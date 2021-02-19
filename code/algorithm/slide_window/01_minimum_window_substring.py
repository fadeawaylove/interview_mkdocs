# 最小覆盖子串
from collections import defaultdict


def min_substring(s, t):
    # 窗口
    window = {x: 0 for x in t}
    # 窗口满足时候的情形
    need = {x: t.count(x) for x in window}

    left = right = 0
    size = len(s)
    valid_cnt = 0
    # 最小子串开始和长度
    start = 0
    len_ = float('inf')
    while right < size:
        # 入窗的字符串
        c = s[right]
        # 窗口右移
        right += 1
        # 对窗口中的数据进行更新
        if c in need:
            window[c] += 1
            if window[c] == need[c]:  # c字符个数满足
                valid_cnt += 1

        print("window: [%s, %s), valid_cnt: %s" % (left, right, valid_cnt))

        # 判断左侧窗口是否要收缩(当前子串满足条件就得收缩左边界)
        while valid_cnt == len(window):
            # 更新最小子串
            if right - left < len_:
                start = left
                len_ = right - left
            # 出窗的字符串
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:  # d字符个数满足
                    valid_cnt -= 1
                window[d] -= 1

    if len_ == float("inf"):
        return ""
    return s[start:start+len_]


print(min_substring("ADOBECODEBANC", "ABC"))
print(min_substring("ADOBECODEBANC", "ABCX"))
