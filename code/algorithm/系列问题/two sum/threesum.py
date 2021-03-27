"""
@Author: 邓润庭
@Time:   2021/3/26 17:56
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            # 从第一个数后面的一个数开始进行two sum
            # 如果每次用全部的nums，就会出现重复的情况
            temp = self.twoSum(nums, i + 1, -num)
            for t in temp:
                ret.append([num] + t)
            while i < n - 1 and nums[i] == nums[i + 1]:  # 避免第一个数字重复
                i += 1
            i += 1
        return ret

    def twoSum(self, nums: List[int], start, target) -> List[List[int]]:
        # nums.sort()
        ret = []
        # 计算两个数的和
        lo = start
        hi = len(nums) - 1
        while lo < hi:
            left = nums[lo]
            right = nums[hi]
            s = left + right
            if s == target:
                ret.append([left, right])
                # while循环避免重复
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
            elif s < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            else:
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return ret


# leetcode上的双指针解法
# 当我们固定第一个数的时候，其实就类似two sum的问题，但是本问题可能有多个，所以考虑用双指针
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        ret = []
        for first in range(n):
            # first不能重复
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # 此时,target就确定了
            target = -nums[first]
            # third初始值设为nums最右边的
            third = n - 1
            second = first + 1
            while second < third:
                # second不能重复
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue

                if third < n - 1 and nums[third] == nums[third + 1]:
                    third -= 1
                    continue

                if nums[second] + nums[third] == target:
                    ret.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                elif nums[second] + nums[third] < target:  # 需要变大
                    second += 1
                else:
                    third -= 1
        return ret


# print(Solution().threeSum(
#     [-1, 0, 1, 2, -1, -4]
# ))

print(Solution2().threeSum(
    [-2, 0, 0, 2, 2]
))
# [[-1,-1,2],[-1,0,1]]
