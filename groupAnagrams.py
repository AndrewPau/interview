"""
Given an array of strings, group anagrams together. Return as a list of lists.
An anagram is defined as words with the same characters but in different order.
"""
def groupAnagrams(strs):
    anagrams = {}
    # Create identifiers of anagrams through a Unicode counter string.
    for string in strs:
        chars = [0 for a in range(256)]
        for l in range(len(string)):
            chars[ord(string[l])] += 1
        word = str(chars)
        # Use the Unicode string as a dictionary key to group anagrams.
        if word in anagrams:
            anagrams[word].append(string)
        else:
            anagrams[word] = [string]
    returnVal = []
    for anagram in anagrams:
        returnVal.append(anagrams[anagram])
    return returnVal

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strings))
