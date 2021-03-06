"""
@Author: 邓润庭
@Time:   2021/3/27 15:24
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if not root:
            return

        # 递归左子树和右子树
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        # 按照题意，替换值
        root.left = None
        root.right = left

        # 将右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right

        p.right = right


class Solution2:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flat(node: TreeNode):
            if not node:
                return node
            # 其实就是先根遍历，然后再加到根节点上
            right = node.right

            # 左子树变为链表，并赋值给node右子树
            node.right = flat(node.left)
            # 原左子树变为空
            node.left = None
            # 找到新右子树的最右节点
            cur = node
            while cur.right:
                cur = cur.right
            cur.right = flat(right)
            return node

        flat(root)
