def maxScore(grid, k):
    m = len(grid)
    n = len(grid[0])
    
    dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
    
    def get_score_cost(val):
        if val == 0:
            return 0, 0
        elif val == 1:
            return 1, 1
        else:  # val == 2
            return 2, 1
    
    score, cost = get_score_cost(grid[0][0])
    if cost <= k:
        dp[0][0][cost] = score
    
    for i in range(m):
        for j in range(n):
            for c in range(k + 1):
                if dp[i][j][c] == -1:
                    continue
                
                if j + 1 < n:
                    s, new_cost = get_score_cost(grid[i][j + 1])
                    if c + new_cost <= k:
                        dp[i][j + 1][c + new_cost] = max(
                            dp[i][j + 1][c + new_cost],
                            dp[i][j][c] + s
                        )
                
                if i + 1 < m:
                    s, new_cost = get_score_cost(grid[i + 1][j])
                    if c + new_cost <= k:
                        dp[i + 1][j][c + new_cost] = max(
                            dp[i + 1][j][c + new_cost],
                            dp[i][j][c] + s
                        )
    
    ans = max(dp[m - 1][n - 1])
    
    return ans if ans != -1 else -1

grid = [[0, 1], [2, 0]]
k = 1

print(maxScore(grid, k))  

grid = [[0, 1],[1, 2]]
k = 1

print(maxScore(grid, k))  

