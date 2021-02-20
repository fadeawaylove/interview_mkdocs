from typing import List


# def maxProfit(prices: List[int]) -> int:
#     days = len(prices)

#     # dp[0][1] 代表第一天 持有着股票 最大利润
#     # dp[0][0] 代表第一天 未持有股票 最大利润
#     # 其余的以此类推
#     dp = [[0, 0] for _ in prices]

#     for i in range(days):
#         if i == 0:
#             dp[0][1] -= prices[0]
#             continue
#         # 今天未持有 = max(昨天未持有， 昨天持有+今天现价)
#         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
#         # 今日持有 = max(昨天持有， -今天现价)
#         dp[i][1] = max(dp[i-1][1], -prices[i])

#     return dp[days-1][0]

def maxProfit(prices: List[int]) -> int:
    dp_i_0 = 0
    dp_i_1 = -prices[0]

    for i in range(1, len(prices)):
        # 今天未持有 = max(昨天未持有， 昨天持有+今天现价)
        dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
        # 今日持有 = max(昨天持有， -今天现价)
        dp_i_1 = max(dp_i_1, -prices[i])

    return dp_i_0


print(maxProfit([7, 1, 5, 3, 6, 4]))
