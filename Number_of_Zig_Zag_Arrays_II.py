MOD = 10**9 + 7

def zigzag_count(n, l, r):
    
    ans = 0

    def dfs(arr):
        nonlocal ans

        if len(arr) == n:
            ans += 1
            return

        for num in range(l, r + 1):

            if arr and arr[-1] == num:
                continue

            if len(arr) >= 2:
                a = arr[-2]
                b = arr[-1]
                c = num

                if (a < b < c) or (a > b > c):
                    continue

            arr.append(num)
            dfs(arr)
            arr.pop()

    dfs([])
    return ans % MOD

print(zigzag_count(3, 1, 3))

print(zigzag_count(3, 4, 5))

