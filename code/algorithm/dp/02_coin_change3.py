# 凑零钱问题
# 比如有1、2、5面额的硬币，每种数量无限，问：给出固定额度，最少需要多少枚？


# 可以自底向上，这时候递归就变为循环
def change_coin(coins, amount):
    # dp[i] = x表示目标金额为i时，最少需要x个硬币
    dp = [amount + 1] * (amount + 1)
    # base case
    dp[0] = 0

    # 接下来其实就是将dp列表填满
    for i in range(amount+1):
        for coin in coins:
            # 无解的情况
            if i-coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i-coin])
    # 如果是初始值，那么说明不存在
    print(dp)
    return -1 if dp[amount] == amount+1 else dp[amount]


print(change_coin([6, 5], 13))
