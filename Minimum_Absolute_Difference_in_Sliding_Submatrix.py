def minDiffSubmatrix(grid, k):
    m = len(grid)
    n = len(grid[0])
    
    result = []
    
    for i in range(m - k + 1):
        row = []
        for j in range(n - k + 1):
            
            values = []
            for x in range(i, i + k):
                for y in range(j, j + k):
                    values.append(grid[x][y])
            
            unique_vals = list(set(values))
            
            if len(unique_vals) <= 1:
                row.append(0)
                continue
            
            unique_vals.sort()
            
            min_diff = float('inf')
            for t in range(1, len(unique_vals)):
                diff = unique_vals[t] - unique_vals[t-1]
                min_diff = min(min_diff, diff)
            
            row.append(min_diff)
        
        result.append(row)
    
    return result

grid = [[1,8],
        [3,-2]]
k = 2

print(minDiffSubmatrix(grid, k))

grid = [[3,-1]]
k = 1

print(minDiffSubmatrix(grid, k))

grid = [[1,-2,3],
        [2,3,5]]
k = 2

print(minDiffSubmatrix(grid, k))

