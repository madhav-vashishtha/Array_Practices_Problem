def reverseWords(s):

    words = s.split()
    
    words.reverse()

    result = " ".join(words)
    
    return result

print(reverseWords("the sky is blue"))

print(reverseWords("  hello world  "))

print(reverseWords("a good   example"))

