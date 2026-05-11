class Solution:
    def separateDigits(self, nums):
        answer = []

        for num in nums:
            for digit in str(num):
                answer.append(int(digit))

        return answer
    
nums = [13, 25, 83, 77]

obj = Solution()
print(obj.separateDigits(nums))

nums = [7,1,3,9]

obj = Solution()
print(obj.separateDigits(nums))

