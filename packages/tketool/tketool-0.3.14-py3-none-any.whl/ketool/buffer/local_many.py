import pickle, os
from typing import Callable, Any

from ketool.JConfig import get_config_obj

import ketool.buffer.bufferbase as bb
from ketool.buffer.bufferbase import buffer


def _load_buffer_file(key):
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    with open(path, 'rb') as f:
        saved_item = pickle.load(f)
    return saved_item


def _save_buffer_file(lists):
    buffer_folder = get_config_obj().get_config("buffer_folder")

    folder = os.path.join(os.getcwd(), buffer_folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    for key, item in lists:
        path = os.path.join(os.getcwd(), buffer_folder, key)
        with open(path, 'wb') as f:
            pickle.dump(item, f)


def _delete_buffer_file(key):
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    if os.path.exists(path):
        os.remove(path)


def _has_buffer_file(key):
    buffer_folder = get_config_obj().get_config("buffer_folder")
    path = os.path.join(os.getcwd(), buffer_folder, key)
    return os.path.exists(path)


bb.has_buffer_file = _has_buffer_file
bb.load_buffer_file = _load_buffer_file
bb.delete_buffer_file = _delete_buffer_file
bb.save_buffer_file = _save_buffer_file
