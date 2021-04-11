"""
@Author: 邓润庭
@Time:   2021/4/6 15:47
"""


# https://leetcode-cn.com/problems/lru-cache/submissions/
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


# hash table + double link list

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    # 将节点移动到末尾的方法
    def _move_node2tail(self, key):
        node = self.hashmap[key]
        # 删除节点
        node.pre.next = node.next
        node.next.pre = node.pre

        # 接到末尾
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    def get(self, key: int) -> int:
        # 如果已经存在于hash map中，则移到最后，变为最新的
        if key in self.hashmap:
            self._move_node2tail(key)
            return self.hashmap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # 添加有几种情况
        if key in self.hashmap:
            # 已经存在，则更新value，然后移到最后
            self.hashmap[key].value = value
            self._move_node2tail(key)
        else:
            # 达到上限，则去掉最少使用的值
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next.pre = None
                self.head.next = self.head.next.next
                self.head.next.pre.next = None
                self.head.next.pre = self.head
            # 添加到末尾最新
            new_node = ListNode(key, value)
            new_node.pre = self.tail.pre
            new_node.next = self.tail
            self.tail.pre.next = new_node
            self.tail.pre = new_node
            self.hashmap[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
