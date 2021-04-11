"""
@Author: 邓润庭
@Time:   2021/4/6 14:27
"""
# https://leetcode-cn.com/problems/count-complete-tree-nodes/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 结合满二叉树和普通二叉树的特点
        hl = 0
        l = root
        while l:
            l = l.left
            hl += 1

        hr = 0
        r = root
        while r:
            r=r.right
            hr += 1

        if hl == hr:

            return 2**hl - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
