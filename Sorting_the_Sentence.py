def sortSentence(s):
    words = s.split()

    words.sort(key=lambda x: int(x[-1]))

    result = []
    for word in words:
        result.append(word[:-1])

    return " ".join(result)

s = "is2 sentence4 This1 a3"
print(sortSentence(s))

s = "Myself2 Me1 I4 and3"
print(sortSentence(s))
