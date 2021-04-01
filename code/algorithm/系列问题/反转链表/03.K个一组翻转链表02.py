"""
@Author: 邓润庭
@Time:   2021/4/1 14:54
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        start = head
        end = head
        # 找到第k个节点，如果不足k，就不反转，直接返回head
        for i in range(k):
            if end is None:
                return head
            end = end.next
        # 反转区间[start, end)
        new_head = self.reverse(start, end)
        # 递归，下一个反转的head就是end
        start.next = self.reverseKGroup(end, k)
        return new_head

    def reverse(self, head: ListNode, tail: ListNode):
        """
        反转一个区间的链表,左闭右开[head, tail)
        :param head: 区间链表的头节点
        :param tail: 区间链表的尾节点
        :return: 反转后的头节点
        """
        pre = None
        cur = head
        while cur != tail:
            next_ = cur.next
            # 改变指向，指向前一个节点
            cur.next = pre
            # 更新前一个节点
            pre = cur
            # 更新当前节点，节点后移
            cur = next_
        return pre
