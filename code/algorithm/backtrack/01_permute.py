# 全排列入门
import copy


def permute(nums):
    res = []

    def backtrack(track):
        # 结束条件
        if len(track) == len(nums):
            res.append(copy.copy(track))
            return

        for num in nums:
            # 排除不合理的选法
            if num in track:
                continue
            # 做选择
            track.append(num)
            # 进入下一层决策树
            backtrack(track)
            # 取消选择
            track.remove(num)

    backtrack([])
    return res


print(permute([1, 2, 3]))
