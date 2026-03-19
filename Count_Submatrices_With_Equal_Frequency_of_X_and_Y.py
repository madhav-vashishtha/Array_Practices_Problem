def countSubmatrices(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    count = 0

    for i in range(rows):
        for j in range(cols):
            
            x_count = 0
            y_count = 0
            
            for r in range(i + 1):
                for c in range(j + 1):
                    if grid[r][c] == 'X':
                        x_count += 1
                    elif grid[r][c] == 'Y':
                        y_count += 1
            
            if x_count == y_count and x_count > 0:
                count += 1

    return count

grid = [["X","Y","."],
        ["Y",".","."]]

print(countSubmatrices(grid))

grid = [["X","X"],
        ["X","Y"]]

print(countSubmatrices(grid))

grid = [[".","."],
        [".","."]]

print(countSubmatrices(grid))






