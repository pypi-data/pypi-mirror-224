#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2023 datavita.com.cn, Inc. All Rights Reserved
#
########################################################################


"""
File: logger.py
Author: wangjiangfeng(wangjiangfeng@hcyjs.com)
Date: 2023/8/14 16:37:56
"""

import logbook
from logbook import Logger, StderrHandler

logbook.set_datetime_format("local")


# patch warn
logbook.base._level_names[logbook.base.WARNING] = 'WARN'


__all__ = [
    "user_log",
    "system_log",
    "user_system_log",
    "release_print"
]


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def user_log_processor(record):
    from fatbulls.environment import Environment
    time = Environment.get_instance().calendar_dt
    if time is not None:
        record.time = time


user_log_group = logbook.LoggerGroup(processor=user_log_processor)


# loggers
# 用户代码logger日志
user_log = Logger("user_log")
# 给用户看的系统日志
user_system_log = Logger("user_system_log")

user_log_group.add_logger(user_log)
user_log_group.add_logger(user_system_log)

# 系统日志
system_log = Logger("system_log")

original_print = print


def init_logger():
    system_log.handlers = [StderrHandler(bubble=True)]
    user_log.handlers = [StderrHandler(bubble=True)]
    user_system_log.handlers = [StderrHandler(bubble=True)]


def user_print(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "")

    message = sep.join(map(str, args)) + end

    user_log.info(message)


def release_print(scope):
    for func in scope.values():
        try:
            if hasattr(func, "__globals__"):
                print_func = func.__globals__.get('print')
                if print_func is not None and print_func.__name__ == user_print.__name__:
                    func.__globals__['print'] = original_print
        except (RuntimeError, AttributeError):
            # DummyFqDataC
            continue
