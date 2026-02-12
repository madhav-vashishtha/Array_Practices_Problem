def groupAnagrams(strs):
    anagram_dict = {}  
    
    for word in strs:
        sorted_word = "".join(sorted(word)) 

        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []

        anagram_dict[sorted_word].append(word)

    return list(anagram_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

strs = [""]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))


