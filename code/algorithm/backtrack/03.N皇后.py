#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03.N皇后.py
@Time    :   2021/04/13 11:55:16
@Author  :   呆瓜 
@Version :   1.0
@Contact :   1032939141@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib


import copy
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 路径、选择列表、退出条件
        board = ["."*n for _ in range(n)]

        def bt(path,startx, ret):
            # 结束条件
            if startx >= n:
                ret.append(path)
                return        
            
            # 选择路径（选择哪一个列）
            for j in range(n):
                if self.check(path, startx, j):
                    new_s = ""
                    for s in range(n):
                        if s == j:
                            new_s += "Q"
                        else:
                            new_s += "."
                    path[startx] = new_s
                    bt(copy.copy(path), startx+1,ret)
                    path[startx] = "."*n
        res = []
        bt(board,0,res)
        return res

    def check(self, board, x, y):
        n = len(board)

        # 检查当前行
        if board[x] != "."*n:
            return False
        # 检查当前列
        for b in board:
            if b[y] != ".":
                return False
        # 检查左上方
        i1,j1=x,y
        while 0<= i1 < n and 0<= j1 < n:
            if board[i1][j1] != ".":
                return False
            i1 -= 1
            j1 -= 1
        # 检查右上方
        m1,k1 = x,y 
        while 0<=m1 < n and 0<=k1<n:
            if board[m1][k1] != ".":
                return False
            m1 -= 1
            k1 += 1

        return True