"""
@Author: 邓润庭
@Time:   2021/4/6 16:21
"""


# 解题思路
# 1.维护一个k->node的哈希map，方便O(1)通过key定位node
# 2.维护一个frequency->DoubleLink的哈希map，通过频率更改node
# 3.维护一个DoubleLink，里面存储的是node


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.frequency = 1
        self.pre = None
        self.next = None


class DLink:
    def __init__(self):
        # 头尾节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def remove(self, node: Node):
        # 移除一个节点
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        return node

    def append(self, node: Node):
        # 尾部添加一个节点
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.size += 1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kn_map = {}
        self.fn_map = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        # 存在
        if key in self.kn_map:
            # 频率要+1
            node: Node = self.kn_map[key]
            self._increase_freq(key)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # 存在，则更新值
        if key in self.kn_map:
            self.kn_map[key].value = value
            self._increase_freq(key)
        else:
            # 容量不足，删除频率最小的一个
            if len(self.kn_map) >= self.capacity:
                self._remove_min_freq()
            # 添加一个新的
            new_node = Node(key, value)
            self.kn_map[key] = new_node
            if new_node.frequency not in self.fn_map:
                self.fn_map[new_node.frequency] = DLink()
            self.fn_map[new_node.frequency].append(new_node)
            self.min_freq = 1

    def _increase_freq(self, key):
        """
        已经存在的节点，频率加1
        :param key:
        :return:
        """
        node: Node = self.kn_map[key]
        # 从原链表移除
        node = self.fn_map[node.frequency].remove(node)
        # 如果移除后，链表变为空的，并且最小频率等于当前节点频率，那么最小频率就要+1
        if node.frequency == self.min_freq and self.fn_map[node.frequency].size == 0:
            self.min_freq += 1
        node.frequency += 1
        # 当前频率不存在，新建一个链表
        if node.frequency not in self.fn_map:
            self.fn_map[node.frequency] = DLink()
        self.fn_map[node.frequency].append(node)

    def _remove_min_freq(self):
        min_dlink = self.fn_map[self.min_freq]
        node = min_dlink.remove(min_dlink.head.next)
        del self.kn_map[node.key]
