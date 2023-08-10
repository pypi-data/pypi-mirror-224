import os


def create_folder_if_not_exsited(*args):
    """
    如果路径下不存在则创建文件夹，返回路径
    :param args: 路径的分段信息，类似os.path.join
    :return: 路径
    """
    path = os.path.join(*args)
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def write_file(path, lines):
    with open(path, 'w') as ff:
        ff.write("\n".join(lines))


def read_file(path):
    with open(path, 'r') as ff:
        return ff.readlines()
