class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        answer = float('inf')

        for target in range(2, 2 * limit + 1):

            moves = 0

            for i in range(n // 2):

                a = nums[i]
                b = nums[n - 1 - i]

                current_sum = a + b

                if current_sum == target:
                    continue

                elif (1 <= target - a <= limit) or (1 <= target - b <= limit):
                    moves += 1

                else:
                    moves += 2

            answer = min(answer, moves)

        return answer
    
obj = Solution()

print(obj.minMoves([1,2,4,3], 4))  
print(obj.minMoves([1,2,2,1], 2))  
print(obj.minMoves([1,2,1,2], 2))   

