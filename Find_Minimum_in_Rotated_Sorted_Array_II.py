def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        elif nums[mid] < nums[right]:
            right = mid

        else:
            right -= 1

    return nums[left]


print(findMin([1, 3, 5]))        
print(findMin([2, 2, 2, 0, 1]))



