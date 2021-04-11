"""
@Author: 邓润庭
@Time:   2021/4/7 20:33
"""
from typing import List

# https://leetcode-cn.com/problems/koko-eating-bananas/submissions/




class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            middle = (left + right) // 2
            if self.can_finish(piles, h, middle):
                right = middle
            else:
                left = middle + 1
        return left

    def can_finish(self, piles, h, s):
        cnt = 0
        for pile in piles:
            t = pile // s
            if pile % s:
                t += 1
            cnt += t
        if cnt <= h:
            return True
        return False


print(Solution().minEatingSpeed(
    [3, 6, 7, 11], 8
))
print(Solution().minEatingSpeed(
    [30, 11, 23, 4, 20], 5
))


