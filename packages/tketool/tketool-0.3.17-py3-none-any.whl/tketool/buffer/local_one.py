import shelve, os
from tketool.JConfig import get_config_obj

import tketool.buffer.bufferbase as bb
from tketool.buffer.bufferbase import buffer

_loaded = False

buffer_folder = get_config_obj().get_config("buffer_folder")
buffer_file_path = os.path.join(os.getcwd(), buffer_folder, "buffer.bin")
shelve_obj = shelve.open(buffer_file_path)


def _load_buffer_file(key):
    return shelve_obj.get(key)


def _save_buffer_file(lists):
    for k, v in lists:
        shelve_obj[k] = v
    shelve_obj.sync()


def _delete_buffer_file(key):
    del shelve_obj[key]
    shelve_obj.sync()


def _has_buffer_file(key):
    return key in shelve_obj


bb.has_buffer_file = _has_buffer_file
bb.load_buffer_file = _load_buffer_file
bb.delete_buffer_file = _delete_buffer_file
bb.save_buffer_file = _save_buffer_file
