# 凑零钱问题
# 比如有1、2、5面额的硬币，每种数量无限，问：给出固定额度，最少需要多少枚？

def change_coin(coins, amount):
    # 优化，减枝（查备忘录）
    memo = {}  # 用个hash table做记录

    # dp[x]表示当前额度为x的时候所需最少的硬币数量
    def dp(x):
        if x in memo:
            return memo[x]

        # base case, 目标金额为0的时候，所需硬币为0；目标金额小于0时，无解
        if x == 0:
            return 0
        if x < 0:
            return -1
        res = float('inf')
        for coin in coins:
            subproblem = dp(x-coin)
            # 子问题无解跳过
            if subproblem == -1:
                continue
            res = min(res, subproblem + 1)
        memo[x] = res if res != float('inf') else -1
        return memo[x]

    return dp(amount)


print(change_coin([1, 2, 5], 24))
