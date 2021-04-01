"""
@Author: 邓润庭
@Time:   2021/3/31 20:56
"""
import functools


def singleton(cls):
    _instance = {}

    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapped


@singleton
class MyClass:
    pass


s1 = MyClass()
s2 = MyClass()

print(id(s1), id(s2))
