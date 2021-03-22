"""
@Author: 邓润庭
@Date:   2021/3/21
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        k = min(k, n // 2)
        if not prices or k == 0:
            return 0
        dp = [[[0] * k, [0] * k] for _ in range(n)]
        # 初始化，第一天买的都为-prices[0]
        dp[0][0] = [-prices[0]] * k
        for i in range(1, n):
            for j in range(0, k):
                # 如果是第一次买直接就是-prices[i]
                # buy_j=max(buy_j, sell_j-1 - price)
                dp[i][0][j] = max(dp[i - 1][0][j], -prices[i] if j == 0 else dp[i - 1][1][j - 1] - prices[i])
                # sell_j=max(sell_j,buy_j + price)
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j] + prices[i])
        return dp[n - 1][1][k - 1]


# print(Solution().maxProfit(3, [2, 4, 1, 10, 9, 8, 20, 13]))
print(Solution().maxProfit(2,
                           [2, 1, 4, 5, 2, 9, 7]))
