"""
Given an array of length N consisting of positions, find the first occurence of a
K group, or return -1 if one does not occur. This can be done in Nlog(N) time.
The elements of P are 1-indexed.
"""
def findKGroup(P, k):
    node = TreeNode(P[0])
    left, right = P[0] - 1, len(P) - P[0]
    if left == k or right == k:
        return 1
    for day in range(1, len(P)):
        left, right = insert(node, P[day], 1, len(P))
        if left == k or right == k:
            return day+1
    return -1

# Insert into node with log(N) time
def insert(node, val, left, right):
    curr = node
    while curr != None:
        if val > curr.val:
            left = curr.val + 1
            if curr.right == None:
                curr.right = TreeNode(val)
                break
            else:
                curr = curr.right
        else:
            right = curr.val - 1
            if curr.left == None:
                curr.left = TreeNode(val)
                break
            else:
                curr = curr.left
    return (val - left, right - val)

# Binary Tree class to perform log(N) insertions
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Should print 4, 2, -1, 9, 7
print(findKGroup([5, 1, 6, 2, 3, 4], 2))
print(findKGroup([1, 2, 3], 1))
print(findKGroup([6, 3, 4, 5, 2, 1], 4))
print(findKGroup([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1))
print(findKGroup([5, 6, 4, 7, 3, 8, 2, 9, 1, 10], 1))
