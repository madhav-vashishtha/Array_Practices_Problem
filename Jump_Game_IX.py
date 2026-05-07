def maxReachable(nums):
    n = len(nums)
    ans = [0] * n

    def dfs(i, visited):
        maximum = nums[i]

        for j in range(n):

            if j > i and nums[j] < nums[i]:
                if j not in visited:
                    visited.add(j)
                    maximum = max(maximum, dfs(j, visited))

            elif j < i and nums[j] > nums[i]:
                if j not in visited:
                    visited.add(j)
                    maximum = max(maximum, dfs(j, visited))

        return maximum

    for i in range(n):
        ans[i] = dfs(i, set([i]))

    return ans


nums = [2, 1, 3]
print(maxReachable(nums))

nums = [2, 3, 1]
print(maxReachable(nums))


