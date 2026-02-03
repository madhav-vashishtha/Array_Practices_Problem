def containsNearbyDuplicate(nums, k):
    last_index = {}  

    for i in range(len(nums)):
        if nums[i] in last_index:
            if i - last_index[nums[i]] <= k:
                return True
        last_index[nums[i]] = i

    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k)) 

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))  

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))  
