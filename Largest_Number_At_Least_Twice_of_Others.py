def dominantIndex(nums):
    largest = max(nums)
    index = nums.index(largest)

    result = True

    for num in nums:
        if num != largest:
            if largest < 2 * num:
                result = False
            
    if result:
        return index
    else:
        return -1
    
print(dominantIndex([3,6,1,0]))
print(dominantIndex([1,2,3,4]))
