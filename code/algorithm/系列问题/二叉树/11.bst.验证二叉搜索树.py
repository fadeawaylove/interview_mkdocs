"""
@Author: 邓润庭
@Time:   2021/4/3 10:24
"""


# https://leetcode-cn.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isvalid(node, minval, maxval):
            if not node:
                return True

            if minval and node.val <= minval.val:
                return False
            if maxval and node.val >= maxval.val:
                return False
            return isvalid(node.left, minval, node) and isvalid(node.right, node, maxval)

        return isvalid(root, None, None)

# 也可以使用中序遍历递增的特性，如果不满足 那么不是bst
