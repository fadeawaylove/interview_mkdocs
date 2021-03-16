from typing import List


# 交易次数为两次


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    k = 2

    dp = [
        [[0, 0] for _ in range(k+1)]
        for _ in range(n)]
    for i in range(0, len(prices)):
        for j in range(k, 0, -1):
            # 处理base case
            if i == 0:
                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i]
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
    return dp[n - 1][k][0]


print(maxProfit(
    [3, 3, 5, 0, 0, 3, 1, 4]
))
