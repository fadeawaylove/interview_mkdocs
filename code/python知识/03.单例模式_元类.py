"""
@Author: 邓润庭
@Time:   2021/3/31 21:05
"""


# SingleTon
# new返回MyClass
# init初始化MyClass的属性
# call的时候MyClass示例化，也就是MyClass()


class SingleTon(type):

    def __init__(cls, cls_name, cls_bases, cls_dict):
        # 给cls加上_instance属性
        if not hasattr(cls, "_instance"):
            cls._instance = None
        super(SingleTon, cls).__init__(cls_name, cls_bases, cls_dict)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingleTon, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=SingleTon):
    pass


s1 = MyClass()
s2 = MyClass()

print(id(s1), id(s2))
