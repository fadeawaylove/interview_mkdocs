"""
@Author: 邓润庭
@Time:   2021/4/7 13:30
"""


# https://leetcode-cn.com/problems/next-greater-element-i/submissions/
# 非常简洁

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret_map = {}
        stack = []
        for x in nums2:
            while stack and x > stack[-1]:
                ret_map[stack.pop()] = x
            stack.append(x)
        return [ret_map.get(x, -1) for x in nums1]
