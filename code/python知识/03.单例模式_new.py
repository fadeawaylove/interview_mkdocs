"""
@Author: 邓润庭
@Time:   2021/3/31 20:40
"""


class SingleTon:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = SingleTon()
s2 = SingleTon()

print(id(s1), id(s2))
# 1566005235664 1566005235664
