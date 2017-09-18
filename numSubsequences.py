"""
Find the number of occurrences of given subsequence in the string.
"""
def numSubsequences(string, sequence):
    matrix = [[0 for a in range(len(string)+1)] for b in range(len(sequence)+1)]
    for a in range(len(string)+1):
        matrix[0][a] = 1

    for a in range(1, len(string)+1):
        for b in range(1, len(sequence)+1):
            # Initialize next value with everything you've found with the given sequence.
            val = matrix[b][a-1]
            # If they match, everything from matrix[b-1][a-1] now becomes valid.
            if string[a-1] == sequence[b-1]:
                val += matrix[b-1][a-1]
            matrix[b][a] = val

    return matrix[len(sequence)][len(string)]

# Prints 2, 4, 6
print(numSubsequences("hotdog", "ho"))
print(numSubsequences("GeeksforGeeks", "Gks"))
print(numSubsequences("numsubsequences", "ses"))
