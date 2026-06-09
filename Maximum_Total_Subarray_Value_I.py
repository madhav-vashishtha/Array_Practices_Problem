def maximumTotalValue(nums, k):
    n = len(nums)
    best = 0

    for i in range(n):
        for j in range(i, n):
            sub = nums[i:j+1]

            value = max(sub) - min(sub)

            if value > best:
                best = value

    return best * k


nums = [1, 3, 2]
k = 2
print(maximumTotalValue(nums, k))   

nums = [4, 2, 5, 1]
k = 3
print(maximumTotalValue(nums, k))  


