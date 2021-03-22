"""
@Author: 邓润庭
@Date:   2021/3/21
"""

from typing import List


# 自底向上，空间优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, n):
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
