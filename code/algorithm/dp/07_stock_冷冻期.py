"""
@Author: 邓润庭
@Time:   2021/3/22 13:57
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        dp = [[0, 0] for _ in range(n)]
        dp[0] = [0, -prices[0]]
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

        for i in range(1, n):
            # 未持有
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i > 1:
                # 持有
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[n - 1][0]


print(Solution().maxProfit(
    [1, 2, 3, 0, 2]
))
