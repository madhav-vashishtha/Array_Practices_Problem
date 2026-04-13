def getMinDistance(nums, target, start):
    min_distance = float('inf')  
    
    for i in range(len(nums)):
        if nums[i] == target:
            distance = abs(i - start)
            if distance < min_distance:
                min_distance = distance
    
    return min_distance

nums = [1,2,3,4,5]
target = 5
start = 3

print(getMinDistance(nums, target, start))

nums = [1]
target = 1
start = 0

print(getMinDistance(nums, target, start))

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0

print(getMinDistance(nums, target, start))


