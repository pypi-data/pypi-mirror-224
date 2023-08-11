from enum import Enum


class log_level_enum(Enum):
    """
    log级别枚举
    """
    Error = 1
    Warning = 2
    normal = 3
    pigeonhole = 4


def log(str, log_level: log_level_enum = log_level_enum.normal):
    """
    打印log
    :param str: log内容
    :param log_level: log级别，使用枚举
    :return: 无返回
    """
    print(f"[{log_level}] {str} \n")
