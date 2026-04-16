def minDistance(nums, queries):
    n = len(nums)
    ans = []
    
    for q in queries:
        target = nums[q]
        min_dist = float('inf')
        
        for j in range(n):
            if j != q and nums[j] == target:
                d = abs(j - q)
                circular_d = n - d
                min_dist = min(min_dist, d, circular_d)
        
        if min_dist == float('inf'):
            ans.append(-1)
        else:
            ans.append(min_dist)
    
    return ans

nums = [1,3,1,4,1,3,2]
queries = [0,3,5]

print(minDistance(nums, queries))

nums = [1,2,3,4]
queries = [0,1,2,3]

print(minDistance(nums, queries))

