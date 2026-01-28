def findMissingElements(nums):
    missing = []

    smallest = min(nums)
    largest = max(nums)

    for num in range(smallest, largest + 1):
        if num not in nums:
            missing.append(num)

    return missing

nums = [1, 4, 2, 5]
print(findMissingElements(nums))

nums = [7,8,6,9]
print(findMissingElements(nums))

nums = [5,1]
print(findMissingElements(nums))
