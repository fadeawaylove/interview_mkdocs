"""
@Author: 邓润庭
@Date:   2021/3/21
"""

from typing import List


# 自顶向下
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dp(n, status):
            # base case
            if n == 0:
                if status == 0:
                    return 0
                else:
                    return -prices[0]
            if status == 0:  # 今日未持有股票
                return max(dp(n - 1, 0), dp(n - 1, 1) + prices[n])
            # 今日持有股票
            return max(dp(n - 1, 1), -prices[n])

        return dp(len(prices) - 1, 0)


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
