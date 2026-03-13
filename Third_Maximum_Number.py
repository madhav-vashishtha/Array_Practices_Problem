def thirdMax(nums):
    nums = list(set(nums))

    nums.sort(reverse=True)

    if len(nums) >= 3:
        return nums[2]
    else:
        return nums[0]
    
nums = [3,2,1]
print(thirdMax(nums))

nums = [1,2]
print(thirdMax(nums))

nums = [2,2,3,1]
print(thirdMax(nums))
