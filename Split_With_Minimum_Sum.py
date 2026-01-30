def splitNum(num):
    digits = list(str(num))
    digits.sort()
    
    num1 = ""
    num2 = ""
    
    for i in range(len(digits)):
        if i % 2 == 0:
            num1 += digits[i]
        else:
            num2 += digits[i]
    
    return int(num1) + int(num2)

print(splitNum(4325))  
print(splitNum(687))  

