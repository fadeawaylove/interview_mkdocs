"""
@Author: 邓润庭
@Time:   2021/3/29 19:32
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 代码看起来不美观，但是可以通过
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        pre, node = self.reverse(k, head)
        return pre

    def raw_reverse(self, head: ListNode):
        # 反转链表
        cur = head
        pre = None
        while cur:
            next_ = cur.next
            # 改变指向，指向前一个节点
            cur.next = pre
            # 更新前一个节点
            pre = cur
            # 更新当前节点，节点后移
            cur = next_
        return pre, head  # 返回当前head和tail节点

    def reverse(self, k, head: ListNode, pre=None):
        # 反转链表
        cnt = k
        cur = head
        while cur and cnt:
            next_ = cur.next
            # 改变指向，指向前一个节点
            cur.next = pre
            # 更新前一个节点
            pre = cur
            # 更新当前节点，节点后移
            cur = next_
            cnt -= 1
        # 如果能正常截取完
        if cnt == 0:
            head.next = self.reverse(k, cur)[0]
        # 不能整除的部分，此时已经反转了，要做处理
        else:
            return self.raw_reverse(pre)
        return pre, head  # 返回当前head和tail节点
