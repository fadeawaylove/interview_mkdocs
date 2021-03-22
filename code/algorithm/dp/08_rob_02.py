"""
@Author: 邓润庭
@Time:   2021/3/22 17:33
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp_pre_1 = max(nums[0], nums[1])  # 前一间
        dp_pre_2 = nums[0]  # 前两间
        for i in range(2, n):
            dp_i = max(dp_pre_1, dp_pre_2+nums[i])
            dp_pre_2 = dp_pre_1
            dp_pre_1 = dp_i
        return dp_pre_1


print(Solution().rob(
    [1, 2, 3, 1]
))
