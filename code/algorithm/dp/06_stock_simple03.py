"""
@Author: 邓润庭
@Date:   2021/3/21
"""

from typing import List


# 自底向上
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [0, -prices[0]]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
