"""
@Author: 邓润庭
@Time:   2021/3/30 11:22
"""


class MyList:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # 返回一个迭代器
        return MyListIterator(self.data)


class MyListIterator:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            ret = self.data[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return ret


a = MyList([1, 2, 3, 4])
for x in a:
    print(x)


class MyList2:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]


for x in MyList2([3, 4, 5, 6]):
    print(x)
