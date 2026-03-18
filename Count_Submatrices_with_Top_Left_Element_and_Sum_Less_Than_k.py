def countSubmatrices(grid, k):
    rows = len(grid)
    cols = len(grid[0])
        
    count = 0
        
    for i in range(rows):
        for j in range(cols):
                
            if i > 0:
                grid[i][j] += grid[i-1][j]
                
            if j > 0:
                grid[i][j] += grid[i][j-1]
                
            if i > 0 and j > 0:
                grid[i][j] -= grid[i-1][j-1]
                
            if grid[i][j] <= k:
                count += 1
        
    return count

grid = [[7,6,3],[6,6,1]]
k = 18

print(countSubmatrices(grid, k))

grid = [[7,2,9],[1,5,0],[2,6,6]]
k = 20
print(countSubmatrices(grid, k))


