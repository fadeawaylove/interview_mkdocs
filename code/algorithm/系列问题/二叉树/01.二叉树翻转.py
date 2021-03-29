"""
@Author: 邓润庭
@Time:   2021/3/27 14:08
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def mirror(node):
            if node:
                node.left, node.right = node.right, node.left
                mirror(node.left)
                mirror(node.right)

        mirror(root)
        return root
