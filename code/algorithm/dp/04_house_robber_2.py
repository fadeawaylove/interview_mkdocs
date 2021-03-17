# https://leetcode-cn.com/problems/house-robber/
from typing import List


# 优化空间
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.cal(nums[:-1]), self.cal(nums[1:]))

    def cal(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp_i2 = nums[0]
        dp_i1 = max(nums[0], nums[1])
        dp_i = dp_i1
        for i in range(2, n):
            dp_i = max(dp_i1, dp_i2 + nums[i])
            dp_i1, dp_i2 = dp_i, dp_i1
        return dp_i


print(Solution().rob([1, 2, 3, 1, 3]))
