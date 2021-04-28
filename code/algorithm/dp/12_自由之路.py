class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)

        index_map = {}
        for i in range(m):
            if ring[i] in key:
                if ring[i] not in index_map:
                    index_map[ring[i]] = []
                index_map[ring[i]].append(i)

        print(index_map)

        def dp(i, j):  # 当前指针指向i 目标字符为j
            # base case
            if j == n:
                return 0

            res = float('inf')
            for k in index_map[key[j]]:
                # 找到最小的下标
                delta = abs(k - i)
                delta = min(delta, m - delta)  # 两个方向取较小

                sub = dp(k, j + 1)
                res = min(res, sub + delta + 1)

            return res

        return (dp(0, 0))


print(Solution().findRotateSteps(
    "godding", "gd"
))