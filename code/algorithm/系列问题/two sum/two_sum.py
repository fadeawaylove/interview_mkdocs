"""
@Author: 邓润庭
@Time:   2021/3/26 16:41
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target) -> List[List[int]]:
        nums.sort()
        ret = []
        # 计算两个数的和
        lo = 0
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


# 返回下标时，可以使用查找表法
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # 1.可以使用暴力循环，两两组合，找到满足的
#         # 2.使用hash表，查找表法
#         d = {}
#         for i,num in enumerate(nums):
#             if target-num in d:
#                 return [d[target-num], i]
#             d[num] = i


print(Solution().twoSum(
    [1, 3, 1, 2, 2, 3], 4
))
print(Solution().twoSum(
    [1, 1, 1, 2, 2, 3, 3], 4
))
