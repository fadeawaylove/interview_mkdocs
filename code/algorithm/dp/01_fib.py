import time


def cst_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        timestrap = end - start
        print('function %s time cost is %s' % (func.__name__, timestrap))
        return ret
    return wrapper

# 斐波那契额数列


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n-1) + fib(n-2)


# 优化1
# 使用一个数组当做备忘录（哈希表也是一样的道理）
def fib2(n, tb):
    if tb[n-1] is not None:
        return tb[n-1]

    if n in (1, 2):
        ret = 1
    else:
        ret = fib2(n-1, tb) + fib2(n-2, tb)
    tb[n-1] = ret
    return ret

# 优化2
# 自底向上
def fib3(n):
    dp = [None] * n
    dp[0] = dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


@cst_time
def test1(n):
    fib(n)


@cst_time
def test2(n):
    fib2(n, [None] * n)


@cst_time
def test3(n):
    fib3(n)


if __name__ == '__main__':
    import sys
    x = int(sys.argv[-1])
    test1(x)
    test2(x)
    test3(x)
