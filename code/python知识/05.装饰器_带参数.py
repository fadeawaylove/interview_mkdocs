"""
@Author: 邓润庭
@Time:   2021/4/2 17:37
"""
import functools
import time
import random


def retry(times, cnt, errors):
    def wrapper(f):

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            for _ in range(cnt):
                try:
                    return f(*args, **kwargs)
                except errors as e:
                    print(e)
                    time.sleep(random.random() * times)

        return wrapped

    return wrapper


@retry(3, 3, (Exception,))
def test():
    raise Exception("ashdja")
    return 111


print(test())
