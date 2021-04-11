"""
@Author: 邓润庭
@Time:   2021/4/11 22:24
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 排序避免重复
        nums.sort()
        n = len(nums)
        distance = 10 ** 7
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            second = first + 1
            third = n - 1
            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if s == target:
                    return s
                if abs(distance - target) > abs(s - target):
                    distance = s
                if s > target:
                    third -= 1
                else:
                    second += 1
        return distance


Solution().threeSumClosest(
    [0, 0, 0],
    1
)
