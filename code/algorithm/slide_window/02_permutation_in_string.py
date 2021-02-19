# 字符串排列
# 当给你一个 S 和一个 T，请问你 S 中是否存在一个子串，包含 T 中所有字符且不包含其他字符？


def permutation_string(s, t):
    window = {x: 0 for x in t}
    need = {x: t.count(x) for x in window}
    len_ = len(s)
    left = right = 0

    valid = 0  # 有效的字母个数
    while right < len_:
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        print("window: [%s, %s)" % (left, right))
        while right-left >= len(t):
            if valid == len(need):
                return True
            d = s[left]
            left += 1
            if d in need:
                if need[d] == window[d]:
                    valid -= 1
                window[d] -= 1

    return False


print(permutation_string("eidbxaooo", "ab"))
