"""
@Author: 邓润庭
@Time:   2021/4/2 8:59
"""


# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 规律是preorder的第一个是root
        # 这样就可以将inorder分为左右两部分
        # 根据inorder的左右两部分的长度，可以将preorder也分为两部分
        # 然后递归操作，每次找到当前的root节点，返回

        def build(pre_start, pre_end, in_start, in_end):
            # base case
            if pre_start > pre_end:
                return

            root_val = preorder[pre_start]
            root_index = inorder.index(root_val)

            left_len = root_index - in_start

            # 递归左右子树
            root = TreeNode(root_val)
            root.left = build(pre_start + 1, pre_start + left_len, in_start, root_index - 1)
            root.right = build(pre_start + left_len + 1, pre_end, root_index + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
