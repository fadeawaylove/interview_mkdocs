"""
@Author: 邓润庭
@Time:   2021/3/22 17:33
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self._rob(root))

    def _rob(self, node):
        if not node:
            return 0,0
        left = self._rob(node.left)
        right = self._rob(node.right)

        # 到每一个节点，都有偷或者不偷两种状态
        # 如果偷当前节点
        is_rob = node.val + left[0] + right[0]
        # 如果不偷当前节点
        not_rob = max(left) + max(right)
        return not_rob,is_rob


