#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   最长回文子串.py
@Time    :   2021/04/14 21:11:39
@Author  :   呆瓜 
@Version :   1.0
@Contact :   1032939141@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 想到双指针
        n=len(s)
        res = ""
        def dp(left, right):
            # 退出条件
            if left > right:
                return
            if self.check(s, left, right):
                nonlocal res
                if len(res) < right-left+1:
                    res = s[left: right+1]
                return
            # 向左右递归
            dp(left+1, right)
            dp(left, right-1)

        dp(0, n-1)
        return res
    
    def check(self, nums, start, end):
        while start < end:
            if nums[start] != nums[end]:
                return False
            start += 1
            end -= 1
        return True


print(Solution().longestPalindrome(
    "abbcccbbbcaaccbababcbcabca"
))