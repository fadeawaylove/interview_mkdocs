# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))

    def dp(self, root: TreeNode):
        if not root:
            return 0, 0
        left = self.dp(root.left)
        right = self.dp(root.right)

        # 抢这家，那么左右下家就不抢
        is_rob = root.val + right[0] + left[0]
        # 这家不抢，取左右下家抢或者不抢的最大值
        not_rob = max(right) + max(left)

        return not_rob, is_rob
