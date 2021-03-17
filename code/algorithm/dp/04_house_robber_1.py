# https://leetcode-cn.com/problems/house-robber/
from typing import List


#
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [[0, 0] for _ in range(n)]  # dp[i][0] dp[i][1]表示到第i个房间偷不偷
#         dp[0][0] = 0
#         dp[0][1] = nums[0]
#         for i in range(1, n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
#             dp[i][1] = dp[i - 1][0] + nums[i]
#
#         return max(dp[n - 1])


# 优化空间
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp_i_0 = 0  # 不偷第i个房间
#         dp_i_1 = nums[0]  # 偷第i个房间
#         for i in range(1, n):
#             dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1), dp_i_0 + nums[i]
#         return max(dp_i_0, dp_i_1)
#
#
# print(Solution().rob([1, 2, 3, 1]))

# 官方思路
# 用 dp[i]表示前i间房屋能偷窃到的最高总金额
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


print(Solution().rob([1, 2, 3, 1]))

# 优化空间
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
#         if n == 2:
#             return max(nums)
#         dp_i2 = nums[0]
#         dp_i1 = max(nums[0], nums[1])
#         for i in range(2, n):
#             dp_i = max(dp_i1, dp_i2 + nums[i])
#             dp_i1, dp_i2 = dp_i, dp_i1
#         return dp_i
#
#
# print(Solution().rob([1, 2, 3, 1]))
