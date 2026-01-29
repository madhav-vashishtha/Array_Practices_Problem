def maxProduct(nums):
    nums.sort()
    
    a = nums[-1]
    b = nums[-2]
    
    return (a - 1) * (b - 1)

print(maxProduct([3, 4, 5, 2]))  
print(maxProduct([1, 5, 4, 5])) 
print(maxProduct([3, 7]))       
