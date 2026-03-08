def findErrorNums(nums):
    n = len(nums)
    duplicate = -1
    missing = -1

    for i in nums:
        if nums.count(i) == 2:
            duplicate = i
            break

    for i in range(1, n+1):
        if i not in nums:
            missing = i
            break

    return [duplicate, missing]


nums = [1,2,2,4]
print(findErrorNums(nums))

nums = [1,1]
print(findErrorNums(nums))

