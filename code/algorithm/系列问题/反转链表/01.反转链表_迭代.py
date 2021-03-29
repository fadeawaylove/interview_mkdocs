"""
@Author: 邓润庭
@Time:   2021/3/27 21:35
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            # 存下下一个节点
            next_ = cur.next
            # 指向前一个节点
            cur.next = pre
            # 更新pre为cur
            pre = cur
            # 更新cur为下一个节点
            cur = next_

        return pre
