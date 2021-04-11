"""
@Author: 邓润庭
@Time:   2021/4/7 21:48
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            middle = (left + right) // 2
            print(left, right, middle)
            if self.can_ship(weights, middle, D):
                right = middle
            else:
                left = middle + 1
        return left

    def can_ship(self, weights, loader, day):
        temp = 0
        cost_day = 1
        for weight in weights:
            if weight > loader:
                return False
            temp += weight
            if temp > loader:
                temp = weight
                cost_day += 1
        return cost_day <= day
