# 最长无重复子串


# def longest_substring(s):
#     left = right = 0

#     # 创建窗口
#     window = {}

#     res = 0
#     ret = 0
#     while right < len(s):
#         c = s[right]
#         right += 1
#         # 1.窗口右移时候，更新哪些数据?
#         if c not in window:
#             window[c] = s.find(c, left)
#             ret += 1
#         else:  # 2.窗口缩小的条件
#             # 3.缩小时更新哪些数据
#             ret = right-left-1
#             res = max(ret, res)
#             left += window[c] + 1
#             window = {x: s.find(x, left) for x in s[left:right]}
#         print(window, left, right)

#     return res

from collections import defaultdict


def longest_substring(s):
    left = right = 0

    # 创建窗口
    window = defaultdict(int)

    res = 0
    while right < len(s):
        c = s[right]
        right += 1
        # 1.窗口右移时候，更新哪些数据?
        window[c] += 1

        # 2.窗口缩小的条件
        while window[c] > 1:
            d = s[left]
            left += 1
            # 3.缩小时更新哪些数据
            window[d] -= 1
        res = max(res, right-left)
    return res


print(longest_substring("aaaaaacxzzc"))
