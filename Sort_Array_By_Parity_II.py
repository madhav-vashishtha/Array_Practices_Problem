def SortArrayByParityII(nums):
    n = len(nums)
    i = 0
    j = 1

    while i < n and j < n:
        if nums[i] % 2 == 1:
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            j += 2
        else:
            i += 2

    return nums

print(SortArrayByParityII([4, 2, 5, 7]))
print(SortArrayByParityII([2, 3]))