def maxDistance(colors):
    n = len(colors)
    max_dist = 0
    
    for i in range(n):
        for j in range(n):
            if colors[i] != colors[j]:
                max_dist = max(max_dist, abs(i - j))
    
    return max_dist

print(maxDistance([1,1,1,6,1,1,1]))

print(maxDistance([1,8,3,8,3]))

print(maxDistance([0,1]))


