"""
@Author: 邓润庭
@Time:   2021/4/7 17:13
"""


# https://leetcode-cn.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        # 将比自己小的都pop出去，那么可以保证是单调递减的
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]

        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # 如果单调队列中最大的那个将要移出窗口，则弹出
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans
