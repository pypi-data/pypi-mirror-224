import pickle, os
from tketool.JConfig import get_config_obj

import tketool.buffer.bufferbase as bb
from tketool.buffer.bufferbase import buffer

_loaded = False


def _load():
    global _loaded

    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, "buffer.bin")
    if os.path.exists(path) and not _loaded:
        _loaded = True
        with open(path, 'rb') as f:
            loadbuffer = pickle.load(f)
            for k, v in loadbuffer.items():
                if k not in bb._buffer_items:
                    bb._buffer_items[k] = v


def _save():
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, "buffer.bin")
    folder = os.path.join(os.getcwd(), buffer_folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(path, 'wb') as f:
        pickle.dump(bb._buffer_items, f)


def _load_buffer_file(key):
    _load()
    return bb._buffer_items(key)


def _save_buffer_file(lists):
    _save()


def _delete_buffer_file(key):
    _load()
    del bb._buffer_items[key]
    _save()


def _has_buffer_file(key):
    _load()
    return key in bb._buffer_items


bb.has_buffer_file = _has_buffer_file
bb.load_buffer_file = _load_buffer_file
bb.delete_buffer_file = _delete_buffer_file
bb.save_buffer_file = _save_buffer_file
