def shortestToChar(s, c):
    result = []

    for i in range(len(s)):
        min_dist = len(s)

        for j in range(len(s)):
            if s[j] == c:
                dist = abs(i - j)
                if dist < min_dist:
                    min_dist = dist

        result.append(min_dist)

    return result

print(shortestToChar("loveleetcode", "e"))
print(shortestToChar("aaab","b"))
