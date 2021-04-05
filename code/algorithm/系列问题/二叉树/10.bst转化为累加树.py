"""
@Author: 邓润庭
@Time:   2021/4/3 10:07
"""


# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 右中左的遍历方式，正好跟中顺遍历相反，便利的时候是从大到小有序的

        sum = 0

        def traverse(node):
            # base case
            if not node:
                return

            traverse(node.right)

            # 代码部分
            nonlocal sum
            sum += node.val
            node.val = sum
            traverse(node.left)
            return node

        return traverse(root)
