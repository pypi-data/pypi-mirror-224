from functools import wraps
from tketool.hash_util import hash_str, hash_obj_strbase
import threading

_buffer_items = {}
_buffer_oper_queue = []

has_buffer_file = None
load_buffer_file = None
delete_buffer_file = None
save_buffer_file = None

flush_freq = 10

buffer_lock = threading.Lock()


def flush():
    if has_buffer_file is None:
        raise Exception("No module imported")

    queue_set = set(_buffer_oper_queue)
    save_item_list = []
    for key in queue_set:
        save_item_list.append((key, _buffer_items[key]))
    save_buffer_file(save_item_list)
    queue_set.clear()



def set_flush_freq(count):
    flush_freq = count


def _get_hash_key_(fun_name, *args, **kwargs):
    key_buffer_ = [hash_str(fun_name)]
    if len(args) > 0:
        key_buffer_.append([hash_obj_strbase(arg) for arg in args])
    if len(kwargs) > 0:
        key_buffer_.append([hash_obj_strbase(kwarg) for kwarg in kwargs])
    return str(fun_name) + "_" + hash_obj_strbase(key_buffer_)


def buffer_item(key: str, value):
    """
    缓存一个对象
    :param key: 对象的key
    :param value: 对象的value
    :return: 无返回
    """
    with buffer_lock:
        nkey = _get_hash_key_(key)
        _buffer_items[nkey] = value
        _buffer_oper_queue.append(nkey)

        if len(_buffer_oper_queue) >= flush_freq:
            flush()
            # print("updata")


def get_buffer_item(key: str):
    """
    获得一个对象的缓存
    :param key: 对象的key
    :return: 对象，查找不到会抛出异常
    """

    if has_buffer_file is None:
        raise Exception("No module imported")

    nkey = _get_hash_key_(key)

    if nkey in _buffer_items:
        return _buffer_items[nkey]

    if has_buffer_file(nkey):
        _buffer_items[key] = load_buffer_file(nkey)
        return _buffer_items[nkey]

    # log_error("没有此buffer item")


def has_item_key(key: str):
    """
    是否存在某个key的缓存对象
    :param key: 缓存的key
    :return: True标识存在
    """

    if has_buffer_file is None:
        raise Exception("No module imported")

    nkey = _get_hash_key_(key)

    if nkey in _buffer_items:
        return True

    if has_buffer_file(nkey):
        return True

    return False


def remove_item(key: str):
    """
    删除某个缓存对象
    :param key: 需要删除对象的key
    :return: 无返回
    """

    if has_buffer_file is None:
        raise Exception("No module imported")

    nkey = _get_hash_key_(key)

    if nkey in _buffer_items:
        del _buffer_items[nkey]
    if has_buffer_file(nkey):
        delete_buffer_file(nkey)


def buffer(version=1.0):
    '''
    缓存方法的标识符
    :param version: 缓存版本
    :return: 无
    '''

    def dector(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global _buffer_items
            nkey = _get_hash_key_(func.__name__, args, kwargs)
            if has_item_key(nkey):
                buffer_value = get_buffer_item(nkey)
                if buffer_value['version'] == version:
                    return buffer_value['value']

            func_result = func(*args, **kwargs)
            buffer_item(nkey, {'version': version, 'value': func_result})

            return func_result

        return wrapper

    return dector
