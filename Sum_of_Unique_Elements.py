def sumOfUnique(nums):
    total = 0

    for num in nums:
        if nums.count(num) == 1:
            total += num

    return total

nums = [1,2,3,2]
print(sumOfUnique(nums))

nums = [1,1,1,1,1]
print(sumOfUnique(nums))

nums = [1,2,3,4,5]
print(sumOfUnique(nums))

