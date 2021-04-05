"""
@Author: 邓润庭
@Time:   2021/4/3 9:52
"""

# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        res = None
        c = 0
        # 中序遍历，就是有序的
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            nonlocal c
            nonlocal res
            c += 1
            # print(node.val, c)
            if c == k:
                res = node.val
            traverse(node.right)

        traverse(root)
        return res