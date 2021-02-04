# 解开密码锁的最少次数
from typing import List


def plus_num(num, index):
    # 往上转一下
    selected_num = int(num[index]) + 1
    next_num = str(selected_num % 10)
    return num[:index] + next_num + num[index+1:]


def minus_num(num, index):
    # 往下转一下
    selected_num = int(num[index]) - 1
    next_num = str(selected_num % 10)
    return num[:index] + next_num + num[index+1:]


def combination_lock(deadends: List[str], target: str):
    if target in deadends:
        return -1
    q = ["0000"]
    visited = []
    visited.extend(deadends)
    steps = 0
    while q:
        size = len(q)
        for _ in range(size):
            cur_num = q.pop(0)
            if cur_num in visited:
                continue
            if cur_num == target:
                return steps

            for i in range(4):
                pnum = plus_num(cur_num, i)
                if pnum not in visited:
                    q.append(plus_num(cur_num, i))
                    visited.append(pnum)
                mnum = minus_num(cur_num, i)
                if pnum not in visited:
                    q.append(mnum)
                    visited.append(mnum)
        steps += 1

    return -1


deadends, target = ["0201", "0101", "0102", "1212", "2002"], "0202"
# deadends, target = ["8888", "0009"]
print(combination_lock(deadends, target))
