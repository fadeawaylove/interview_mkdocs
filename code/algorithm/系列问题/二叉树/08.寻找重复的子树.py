"""
@Author: 邓润庭
@Time:   2021/4/2 9:29
"""
# https://leetcode-cn.com/problems/find-duplicate-subtrees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        res = []
        memo = {}


        def traverse(node: TreeNode):

            if not node:
                return '#'

            left = traverse(node.left)
            right = traverse(node.right)

            n = f"{left},{right},{node.val}"

            cnt = memo.get(n, 0)
            if cnt == 1:
                res.append(node)
            memo[n] = cnt + 1
            return n

        traverse(root)
        return res






