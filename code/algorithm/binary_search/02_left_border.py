# 查找左边界


def search_left_border(nums, target):
    left = 0
    right = len(nums) - 1

    # 区间相当于[left, right]，两端闭合
    while left <= right:  # 循环终止条件为left=right+1
        mid = (right+left)//2
        if target > nums[mid]:
            # 搜索区间变为[mid+1, right]
            left = mid + 1
        elif target < nums[mid]:
            # 搜索区间变为[left, mid-1]
            right = mid - 1
        else:
            # 向左收缩区间
            right = mid - 1
    # 检查越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


print(search_left_border([1, 4, 5, 5, 5, 5, 7, 9, 22], 22))
