def minimumDistance(nums):
    from collections import defaultdict
    
    index_map = defaultdict(list)
    
    for i, num in enumerate(nums):
        index_map[num].append(i)
    
    ans = float('inf')
    
    for indices in index_map.values():
        if len(indices) >= 3:
            for i in range(len(indices) - 2):
                i1 = indices[i]
                i3 = indices[i + 2]
                
                distance = 2 * (i3 - i1)
                ans = min(ans, distance)
    
    return ans if ans != float('inf') else -1

nums = [1,2,1,1,3]
print(minimumDistance(nums))

nums = [1,1,2,3,2,1,2]
print(minimumDistance(nums))

nums = [1]
print(minimumDistance(nums))

