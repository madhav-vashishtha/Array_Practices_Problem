def distance(nums):
    n = len(nums)
    arr = [0] * n
    
    pos = {}
    for i in range(n):
        if nums[i] not in pos:
            pos[nums[i]] = []
        pos[nums[i]].append(i)
    
    for i in range(n):
        same_indices = pos[nums[i]]
        
        total = 0
        for j in same_indices:
            if i != j:
                total += abs(i - j)
        
        arr[i] = total
    
    return arr

nums = [1,3,1,1,2]
print(distance(nums))

nums = [0,5,3]
print(distance(nums))



