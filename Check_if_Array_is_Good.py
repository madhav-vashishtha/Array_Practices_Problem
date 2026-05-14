class Solution:
    def isGood(self, nums):
        nums.sort()   
        
        n = nums[-1]  
        
        if len(nums) != n + 1:
            return False
        
        for i in range(1, n):
            if nums[i - 1] != i:
                return False
        
        if nums[-1] == n and nums[-2] == n:
            return True
        
        return False
    
obj = Solution()

print(obj.isGood([1, 3, 3, 2]))  
print(obj.isGood([2, 1, 3]))     
print(obj.isGood([1, 1]))         


