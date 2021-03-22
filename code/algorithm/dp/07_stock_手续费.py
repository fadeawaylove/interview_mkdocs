"""
@Author: 邓润庭
@Time:   2021/3/22 13:57
"""
from typing import List


# 自底向上，空间优化
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, n):
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]-fee), max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0


print(Solution().maxProfit(
    prices=[1, 3, 2, 8, 4, 9],
    fee=2
))
