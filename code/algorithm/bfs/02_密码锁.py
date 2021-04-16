class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = ["0000"]
        visited = []
        cnt = 0
        while q:
            sq = len(q)
            for i in range(sq):
                num = q.pop(0)
                if num in deadends:
                    continue
                # 目标
                if num == target:
                    return cnt
                # 扩散
                for i in range(4):
                    t1 = self.num_up(num, i)
                    if t1 not in visited:
                        q.append(t1)
                        visited.append(t1)
                    t2 = self.num_down(num, i)
                    if t2 not in visited:
                        q.append(t2)
                        visited.append(t2)

            cnt += 1
        return -1

    
    def num_up(self,num, index):
        n = (int(num[index]) + 1) % 10
        num = list(num)
        num[index] = str(n)
        num = "".join(num)
        return num
    
    def num_down(self,num, index):
        n = (int(num[index]) - 1) % 10
        num = list(num)
        num[index] = str(n)
        num = "".join(num)
        return num