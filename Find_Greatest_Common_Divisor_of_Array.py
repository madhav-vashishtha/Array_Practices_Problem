def findGCD(nums):
    smallest = min(nums)
    largest = max(nums)

    while largest % smallest != 0:
        largest, smallest = smallest, largest % smallest

    return smallest

print(findGCD([2,5,6,9,10])) 
print(findGCD([7,5,6,8,3]))  
print(findGCD([3,3]))      


