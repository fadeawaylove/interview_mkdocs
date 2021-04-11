"""
@Author: 邓润庭
@Time:   2021/4/7 11:00
"""

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 默认是最小堆
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # 一开始都为空，往小顶堆加
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
        # 小堆的数字都大于大堆
        else:  # 都是满的
            if num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

        # 两边个数差距不大于1
        while len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        while len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if self.min_heap and self.max_heap:
            if len(self.min_heap) == len(self.max_heap):
                return (self.min_heap[0] - self.max_heap[0]) / 2
        if self.min_heap:
            return self.min_heap[0]
