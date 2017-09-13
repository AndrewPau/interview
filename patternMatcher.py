"""
Returns whether the given string can be represented by the pattern sequence.
string - GraphGraphGraph
pattern - aaa
"""
def findPattern(string, pattern):
	mappings = {}
	return helper(string, 0, pattern, 0, mappings)

def helper(string, index, pattern, pos, mappings):
	if pos == len(pattern) and index == len(string):
		return True
	elif pos == len(pattern) or index == len(string):
		return False
	if pattern[pos] in mappings:
		val = mappings[pattern[pos]]
		if len(val) + index > len(string) or string[index:index+len(val)] != val:
			return False
		return helper(string, index + len(val), pattern, pos + 1, mappings)
	for a in range(len(string)):
		mappings[pattern[pos]] = string[index:index+a+1]
		if helper(string, index+a+1, pattern, pos+1, mappings):
			return True
		del mappings[pattern[pos]]
	return False

# Testing - Should print True, False, True, True
print(findPattern("GraphGraphGraph", "aaa"))
print(findPattern("hey", "aa"))
print(findPattern("OhMyGod", "abc"))
print(findPattern("OhMyOhOhHey", "abaac"))
