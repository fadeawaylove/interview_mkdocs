# https://leetcode-cn.com/problems/remove-covered-intervals/solution/
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[-1]))

        count = 0
        pre_end = 0
        for _, end in intervals:
            if end > pre_end:
                count += 1
                pre_end = end
        return count

print(Solution().removeCoveredIntervals(
    [[1, 4], [3, 6], [2, 8], [1, 2]]
))
