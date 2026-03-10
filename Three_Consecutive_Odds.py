def threeConsecutiveOdds(arr):
    count = 0
    
    for num in arr:
        if num % 2 != 0:  
            count += 1
            if count == 3:
                return True
        else:
            count = 0      
    
    return False

arr = [2,6,4,1]
print(threeConsecutiveOdds(arr))

arr = [1,2,34,3,4,5,7,23,12]
print(threeConsecutiveOdds(arr))
