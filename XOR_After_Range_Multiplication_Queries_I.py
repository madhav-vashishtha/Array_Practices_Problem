def solve(nums, queries):
    MOD = 10**9 + 7

    for li, ri, ki, vi in queries:
        idx = li
        while idx <= ri:
            nums[idx] = (nums[idx] * vi) % MOD
            idx += ki

    result = 0
    for num in nums:
        result ^= num

    return result

nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]

print(solve(nums, queries))

nums = [1,1,1]
queries = [[0,2,1,4]]

print(solve(nums, queries))
