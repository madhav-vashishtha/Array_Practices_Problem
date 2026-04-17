def reverse_num(x):
    return int(str(x)[::-1])   

def minMirrorDistance(nums):
    n = len(nums)
    min_dist = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            if reverse_num(nums[i]) == nums[j]:
                min_dist = min(min_dist, j - i)
    
    return min_dist if min_dist != float('inf') else -1


print(minMirrorDistance([12,21,45,33,54]))  
print(minMirrorDistance([120,21]))  
print(minMirrorDistance([21,120])) 
