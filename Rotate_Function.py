def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)
    
    F = 0
    for i in range(n):
        F += i * nums[i]
    
    max_value = F
    
    for k in range(1, n):
        F = F + total_sum - n * nums[n - k]
        max_value = max(max_value, F)
    
    return max_value

nums = [4, 3, 2, 6]
print(maxRotateFunction(nums))

nums = [100]
print(maxRotateFunction(nums))


