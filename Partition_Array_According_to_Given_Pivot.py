class Solution:
    def pivotArray(self, nums, pivot):
        smaller = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return smaller + equal + greater
    
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

sol = Solution()
print(sol.pivotArray(nums, pivot))

nums = [-3,4,3,2]
pivot = 2

sol = Solution()
print(sol.pivotArray(nums, pivot))



