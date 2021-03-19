"""
@Author: 邓润庭
@Date:   2021/3/19
"""

from typing import List


# 自底向上
def min_coin_num(coins: List, amount: int):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for n in range(amount + 1):
        for coin in coins:
            if coin <= n:
                dp[n] = min(dp[n], dp[n - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


print(min_coin_num([1, 2, 5], 6))
