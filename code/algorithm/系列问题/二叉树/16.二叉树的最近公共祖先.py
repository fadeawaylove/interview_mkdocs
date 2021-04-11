"""
@Author: 邓润庭
@Time:   2021/4/6 13:53
"""


# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # base case
        if not root or root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果left和right都不为空，说明p q分别在root的左右子树中，root就是最近祖先
        if left and right:
            return root
        # 如果都为空，说明root不是公共祖先
        if not left and not right:
            return None
        # 其一不为空
        return left or right
