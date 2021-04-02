"""
@Author: 邓润庭
@Time:   2021/4/2 16:14
"""


def multiply():
    return (lambda x: i * x for i in range(4))


print(multiply())

print([m(100) for m in multiply()])


def multiply2():
    ret = []
    for i in range(4):
        def inner(x):
            return x * i

        ret.append(inner)

    return ret


print([m(100) for m in multiply2()])


