from typing import List


# 每次交易要支付手续费，只要把手续费从利润中减去即可
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。


def maxProfit(prices: List[int], fee: int) -> int:
    dp_i_0 = 0  # 今天未持有股票的最大利润
    dp_i_1 = -prices[0]  # 今天持有股票的最大利润

    for i in range(0, len(prices)):
        temp = dp_i_0
        # 今天未持有 = max(昨天未持有， 昨天持有+今天现价)
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)  # 卖出的时候才计算手续费
        # 今日持有 = max(昨天持有， 昨天未持有-今天现价)
        dp_i_1 = max(dp_i_1, temp - prices[i])

    return dp_i_0


print(maxProfit([1, 3, 2, 8, 4, 9], 2))
