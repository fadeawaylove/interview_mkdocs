"""
@Author: 邓润庭
@Date:   2021/3/21
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 初始状态设置
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1+prices[i])
            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(sell2, buy2+prices[i])
        return sell2


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
