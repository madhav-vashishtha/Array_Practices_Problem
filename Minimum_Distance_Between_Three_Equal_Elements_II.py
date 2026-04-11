def minDistance(nums):
    from collections import defaultdict
    
    index_map = defaultdict(list)
    
    for i in range(len(nums)):
        index_map[nums[i]].append(i)
    
    min_dist = float('inf')
    
    for key in index_map:
        indices = index_map[key]
        
        if len(indices) >= 3:
            for i in range(len(indices) - 2):
                a = indices[i]
                b = indices[i + 1]
                c = indices[i + 2]
                
                dist = abs(a - b) + abs(b - c) + abs(c - a)
                min_dist = min(min_dist, dist)
    
    return min_dist if min_dist != float('inf') else -1

nums = [1,2,1,1,3]
print(minDistance(nums))  

nums = [1,1,2,3,2,1,2]
print(minDistance(nums))  

nums = [1]
print(minDistance(nums))  


