"""
@Author: 邓润庭
@Time:   2021/4/3 10:48
"""


# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def traverse(node):
            if not node:
                return

            if node.val == val:
                return node

            if node.val < val:
                return traverse(node.right)

            if node.val > val:
                return traverse(node.left)

        return traverse(root)
