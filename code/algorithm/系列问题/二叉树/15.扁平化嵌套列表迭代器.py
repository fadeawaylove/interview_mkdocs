"""
@Author: 邓润庭
@Time:   2021/4/5 22:06
"""
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = nestedList

    def next(self) -> int:

        return self.data.pop(0).getInteger()


    def hasNext(self) -> bool:
        # 第一个是列表，则循环插进去
        while self.data and not self.data[0].isInteger():
            fisrt = self.data.pop(0).getList()
            print(fisrt)
            for x in fisrt[::-1]:
                self.data.insert(0, x)
        return len(self.data) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())