# 最基础的二分查找


def search(nums, target):
    left = 0
    right = len(nums) - 1

    # 区间相当于[left, right]，两端闭合
    while left <= right:
        mid = (right+left)//2
        if target > nums[mid]:
            # 搜索区间变为[mid+1, right]
            left = mid + 1
        elif target < nums[mid]:
            # 搜索区间变为[left, mid-1]
            right = mid - 1
        else:
            return mid
    return -1


print(search([1, 4, 5, 7, 9, 22], 4))
