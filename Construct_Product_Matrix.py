def constructProductMatrix(grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])

        nums = [grid[i][j] for i in range(n) for j in range(m)]

        size = len(nums)

        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * nums[i-1]) % MOD

        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * nums[i+1]) % MOD

        res = [0] * size
        for i in range(size):
            res[i] = (prefix[i] * suffix[i]) % MOD

        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(res[idx])
                idx += 1
            ans.append(row)

        return ans

grid = [[1,2],[3,4]]

print(constructProductMatrix(grid))

grid = [[12345],[2],[1]]

print(constructProductMatrix(grid))






