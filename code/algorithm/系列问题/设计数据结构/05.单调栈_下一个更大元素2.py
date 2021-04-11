"""
@Author: 邓润庭
@Time:   2021/4/7 13:30
"""


# https://leetcode-cn.com/problems/next-greater-element-ii/submissions/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 可以一直循环搜索，直到当前要求的是最大的那个数
        stack = []
        # 为了避免重复，使用下标存储结果
        n = len(nums)
        ret = [-1] * n
        for i, x in enumerate(nums * 2):
            if i > n - 1:
                i = i - n
            while stack and x > nums[stack[-1]]:
                index = stack.pop()
                if ret[index] == -1:
                    ret[index] = x
            stack.append(i)
        return ret
