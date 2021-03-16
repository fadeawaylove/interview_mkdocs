from typing import List


# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)


def maxProfit(prices: List[int]) -> int:
    dp_i_0 = 0  # 今天未持有股票的最大利润
    dp_i_1 = -prices[0]  # 今天持有股票的最大利润
    dp_pre_0 = 0  # 前天未持有股票的最大利润

    for i in range(1, len(prices)):
        temp = dp_i_0  # 昨天未持有
        # 今天未持有 = max(昨天未持有， 昨天持有+今天现价)
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        # 今日持有 = max(昨天持有， 前天未持有-今天现价)
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
        dp_pre_0 = temp  # 下一次就变为前天的未持有

    return dp_i_0


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 0, 2]))
