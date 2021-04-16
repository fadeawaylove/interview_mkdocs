#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1109. 航班预订统计.py
@Time    :   2021/04/14 09:15:27
@Author  :   呆瓜 
@Version :   1.0
@Contact :   1032939141@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0 for _ in range(n)]

        for book in bookings:
            i,j,k = book
            nums[i-1] += k
            if j < n:
                nums[j] -= k
        for i in range(n):
            if i > 0:
                nums[i] += nums[i-1]            
        return nums


print(Solution().corpFlightBookings(
   [[1,2,10],[2,2,15]],2
))