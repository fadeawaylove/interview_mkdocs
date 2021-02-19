# 找所有字母异位词
# 这是 LeetCode 第 438 题，Find All Anagrams in a String，难度 Medium


def permutation_string(s, t):
    window = {x: 0 for x in t}
    need = {x: t.count(x) for x in window}
    len_ = len(s)
    left = right = 0

    ret = []
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
                ret.append(left)
            d = s[left]
            left += 1
            if d in need:
                if need[d] == window[d]:
                    valid -= 1
                window[d] -= 1

    return ret


print(permutation_string("cbaebabacd", "abc"))
