def maxNumberOfBalloons(text):
    b = text.count('b')
    a = text.count('a')
    l = text.count('l') // 2
    o = text.count('o') // 2
    n = text.count('n')

    return min(b, a, l, o, n)


print(maxNumberOfBalloons("nlaebolko"))        
print(maxNumberOfBalloons("loonbalxballpoon")) 
print(maxNumberOfBalloons("leetcode"))          

