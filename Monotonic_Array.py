def isMonotonic(nums):
    increasing = True
    decreasing = True
    
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            increasing = False
        if nums[i] < nums[i + 1]:
            decreasing = False
    
    return increasing or decreasing


print(isMonotonic([1,2,2,3]))   
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))  


