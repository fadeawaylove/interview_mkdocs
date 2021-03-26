"""
@Author: 邓润庭
@Time:   2021/3/23 10:53
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        dp_i = 1
        for i in range(1, n+1):
            print(dp_i)
            temp = 9
            j = 0
            while j < i-1:
                temp *= (9 - j)
                j += 1
            dp_i += temp
        return dp_i


print(Solution().countNumbersWithUniqueDigits(3))
