


def partition(nums, i, j):
    pivot = nums[i]
    while i < j:
        while i < j and pivot <= nums[j]:  # 找到右边第一个小于pivot的数
            j -= 1
        nums[i] = nums[j]

        while i < j and pivot >= nums[i]:  # 找到左边第一个大于pivot的数
            i += 1
        nums[j] = nums[i]
    # 循环结束时,i=j,同时也是最后的下标，更新下分割点的值为pivot
    nums[j] = pivot
    return j

def quciksort(nums, lo, hi):
    if lo >= hi:
        return
    p = partition(nums, lo, hi)
    quciksort(nums, lo, p-1)
    quciksort(nums, p+1, hi)
    return nums


print(quciksort([3,2,3,1,2,4,5,5,6], 0, 8))

