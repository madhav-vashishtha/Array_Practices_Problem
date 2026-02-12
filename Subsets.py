def subsets(nums):
    result = [[]]  

    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        result.extend(new_subsets)

    return result


nums = [1, 2, 3]
print(subsets(nums))

nums = [0]
print(subsets(nums))

