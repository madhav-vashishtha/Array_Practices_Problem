def maxScore(grid):
    n = len(grid)
    
    prefix = [[0]*n for _ in range(n)]
    
    for j in range(n):
        prefix[0][j] = grid[0][j]
        for i in range(1, n):
            prefix[i][j] = prefix[i-1][j] + grid[i][j]
    
    def get_sum(j, l, r):
        if l > r:
            return 0
        return prefix[r][j] - (prefix[l-1][j] if l > 0 else 0)
    
    res = 0
    
    for mask in range(n**n):  
        heights = []
        temp = mask
        
        for _ in range(n):
            heights.append(temp % n)
            temp //= n
        
        score = 0
        
        for j in range(n):
            for i in range(heights[j] + 1, n):
                left_black = (j > 0 and heights[j-1] >= i)
                right_black = (j < n-1 and heights[j+1] >= i)
                
                if left_black or right_black:
                    score += grid[i][j]
        
        res = max(res, score)
    
    return res

grid = [[0,0,0,0,0],
        [0,0,3,0,0],
        [0,1,0,0,0],
        [5,0,0,3,0],
        [0,0,0,0,2]]

print(maxScore(grid))

grid = [[10,9,0,0,15],
        [7,1,0,8,0],
        [5,20,0,11,0],
        [0,0,0,1,2],
        [8,12,1,10,3]]

print(maxScore(grid))


