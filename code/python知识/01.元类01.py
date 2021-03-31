"""
@Author: 邓润庭
@Time:   2021/3/30 9:43
"""


class DocCheckMetaClass(type):
    """
    1.类必须有文档注释,不能为空
    2.在一个类内部定义的所有函数必须有文档注释,不能为空。
    """

    def __init__(cls, cls_name, cls_bases, cls_dict: dict):
        # 检查类的文档注释
        if "__doc__" not in cls_dict or not cls_dict["__doc__"].strip():
            raise Exception("class [%s] must have a doc." % (cls_name,))
        # 检查方法是否有文档注释
        for k, v in cls_dict.items():
            if k.startswith("__"):
                continue
            if not callable(v):
                continue
            if not v.__doc__ or not v.__doc__.strip():
                raise Exception("method [%s] must have a doc." % (v,))

        super().__init__(cls_name, cls_bases, cls_dict)


class Person(metaclass=DocCheckMetaClass):
    """Person类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        """   """
        print("我是：%s，今年：%s" % (self.name, self.age))
