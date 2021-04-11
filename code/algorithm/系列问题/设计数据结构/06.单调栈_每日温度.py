"""
@Author: 邓润庭
@Time:   2021/4/7 16:32
"""


# https://leetcode-cn.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []  # stack存储下标
        n = len(T)
        ret = [0] * n
        for i in range(n):
            t = T[i]
            while stack and t > T[stack[-1]]:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret
