def shortestDistance(words, target, startIndex):
    n = len(words)
    ans = float('inf')
    
    for i in range(n):
        if words[i] == target:
            forward = (i - startIndex) % n
            backward = (startIndex - i) % n
            ans = min(ans, forward, backward)
    
    return ans if ans != float('inf') else -1

words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1

print(shortestDistance(words, target, startIndex))

words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0

print(shortestDistance(words, target, startIndex))

words = ["i","eat","leetcode"]
target = "ate"
startIndex = 0

print(shortestDistance(words, target, startIndex))

