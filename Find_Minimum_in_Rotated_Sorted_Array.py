class Solution:
    def findMin(self, arr):

        s, e = 0, len(arr) - 1

        while s < e:

            mid = s + (e - s) // 2

            if arr[mid] > arr[e]:
                s = mid + 1

            else:
                e = mid

        return arr[s]
    
obj = Solution()

print(obj.findMin([3,4,5,1,2]))
print(obj.findMin([4,5,6,7,0,1,2]))
print(obj.findMin([11,13,15,17]))


