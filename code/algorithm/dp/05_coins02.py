"""
@Author: 邓润庭
@Date:   2021/3/19
"""

from typing import List


# 备忘录优化
def min_coin_num(coins: List, amount: int):
    memo = [None] * (amount + 1)

    def dp(n):
        if memo[n] is not None:
            return memo[n]

        # 边界条件
        if n == 0:  # 金额为0，不需要硬币了
            return 0
        if n < 0:  # 金额为负了，当前递归子节点无解
            return -1
        ret = float("inf")
        for coin in coins:
            sub_problem = dp(n - coin)
            if sub_problem == -1:
                continue
            ret = min(ret, sub_problem + 1)
        # 记入备忘录
        memo[n] = ret if ret != float("inf") else -1
        return memo[n]

    return dp(amount)


print(min_coin_num([1, 2, 5], 21))
