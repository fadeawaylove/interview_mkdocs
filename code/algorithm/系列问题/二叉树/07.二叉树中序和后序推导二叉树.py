"""
@Author: 邓润庭
@Time:   2021/4/2 9:01
"""


# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(instart, inend, poststart, postend):
            # base case
            if poststart > postend:
                return

            root = TreeNode(postorder[postend])
            index = inorder.index(root.val)

            left_size = index - instart

            # 子结果
            root.left = build(instart, index - 1, poststart, poststart + left_size - 1)
            root.right = build(index + 1, inend, poststart + left_size, postend - 1)

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
