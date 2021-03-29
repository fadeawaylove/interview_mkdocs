"""
@Author: 邓润庭
@Time:   2021/3/27 15:47
"""
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # base case
        if not root:
            return

        # 具体操作
        # 确定left的next
        if root.left:
            root.left.next = root.right
        # 确定right的next
        if root.next and root.right:
            root.right.next = root.next.left

        # 递归左右子树
        self.connect(root.left)
        self.connect(root.right)

        return root
