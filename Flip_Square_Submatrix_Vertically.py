def flipSubmatrix(grid, x, y, k):
    for i in range(k // 2):
        r1 = x + i
        r2 = x + k - 1 - i
        
        for j in range(y, y + k):
            grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]
    
    return grid

grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
x = 1
y = 0
k = 3
print(flipSubmatrix(grid, x, y, k))

grid = [[3,4,2,3],
        [2,3,4,2]]
x = 0
y = 2
k = 2
print(flipSubmatrix(grid, x, y, k))
