def minOperations(grid, x):
    nums = []
    for row in grid:
        for val in row:
            nums.append(val)
    
    remainder = nums[0] % x
    for num in nums:
        if num % x != remainder:
            return -1
    
    nums.sort()
    median = nums[len(nums) // 2]
    
    operations = 0
    for num in nums:
        operations += abs(num - median) // x
    
    return operations

grid = [[2,4],[6,8]]
x = 2
print(minOperations(grid, x))

grid = [[1,5],[2,3]]
x = 1
print(minOperations(grid, x))

grid = [[1,2],[3,4]]
x = 2
print(minOperations(grid, x))

