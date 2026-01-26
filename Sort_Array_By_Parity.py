def sortArrayByParity(nums):
    even = []
    odd = []


    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even + odd

nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))

nums = [0]
print(sortArrayByParity(nums))

    