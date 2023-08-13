#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import decimal
from functools import wraps
import datetime
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
ch1r = logging.StreamHandler()
ch1r.setFormatter(formatter)
logger.addHandler(ch1r)



def single(cls):
    """
    类装饰器,对类实现单例模式,
    在类上使用@warpper进行调用
    :param cls:
    :return:
    """
    def inner(*args, **kwargs):
        if not hasattr(cls, "ins"):
            instance = cls(*args, **kwargs)
            setattr(cls, "ins", instance)
        return getattr(cls, "ins")
    return inner

def retry(max_retry: int = 0):
    """
    重试装饰器,调用成功返回原函数的返回值,调用失败或超过重试次数则返回False
    :param max_retry: 重试次数,默认为0
    :return:
    """
    def warpp(func):
        @wraps(func)
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            number = 0
            if not ret:
                while number < max_retry:
                    number += 1
                    print(f"共计进行{max_retry}次重试,现在开始进行第:{number}次重试")
                    result = func(*args, **kwargs)
                    if result:
                        return result
                return False
            else:
                return ret
        return inner
    return warpp


def timer(func, unit="s"):
    """
    计算函数的运行时间—单位s,传递ms，则打印毫秒
    :param func: 被装饰的函数
    :return:None
    """
    def call_fun(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        if unit == "s":
            print('%s() run time：%s s' %
                  (func.__name__, int(end_time - start_time)))
        else:
            print('%s() run time：%s ms' %
                  (func.__name__, int(1000 * (end_time - start_time))))
        return f
    return call_fun


def log(func):
    def inner(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        res = func(*args, **kwargs)
        logger.debug(f"func: {func.__name__} {args} -> {res}")
        return res
    return inner

