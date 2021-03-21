"""
@Author: 邓润庭
@Date:   2021/3/21
"""

from typing import List


# 自顶向下
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(prices))]
        memo[0] = 0, -prices[0]

        def dp(n, status):
            # base case
            if memo[n][status] is not None:
                return memo[n][status]
            else:
                if status == 0:  # 今日未持有股票
                    ret = max(dp(n - 1, 0), dp(n - 1, 1) + prices[n])
                else:
                    # 今日持有股票
                    ret = max(dp(n - 1, 1), -prices[n])
                memo[n][status] = ret
                return ret

        return dp(len(prices) - 1, 0)


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
