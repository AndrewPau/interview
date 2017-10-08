"""
Given a tree of height h constructed with integers
[1...(2^h)-1] in postorder traversal, find the integers
who are direct parents of each value in q,
or -1 if the value is the root's.
"""
def answer(h, q):
    retVal = []
    for converter in q:
        currHeight = h
        prev = -1
        start = 1
        end = (2**currHeight)-1
        # Find the value in the binary tree. Each level traversal will
        # get rid of 2^(currHeight-1) entries.
        while converter != end:
            prev = end
            # Go down right branch
            if converter >= start + 2**(currHeight-1) - 1:
                start = start + 2**(currHeight-1) - 1
                end -= 1
            # Go down left branch
            else:
                end = end - 2**(currHeight-1)
            currHeight -= 1
        retVal.append(prev)
    return retVal
