"""
Given a binary tree, find the k-th largest element in the binary tree.
"""
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

currNode = 0

# Finds the k-th largest element by scanning the right, middle, and left.
def kthLargestElem(node, k):
    global currNode
    # Base case
    if node == None:
        return None
    # Traverse the right side first
    val = kthLargestElem(node.right, k)
    if val != None:
        return val
    # Check the current node
    currNode += 1
    if k == currNode:
        return node.val
    # Traverse the left side last
    val = kthLargestElem(node.left, k)
    if val != None:
        return val
    # Return -1 if k is larger than the number of elements in the tree.
    return None

t = Tree(100)
t.left = Tree(50)
t.left.left = Tree(25)
t.left.right = Tree(75)
t.right = Tree(200)
t.right.left = Tree(150)
t.right.right = Tree(250)

# Testing
print(kthLargestElem(t, 1))
currNode = 0
print(kthLargestElem(t, 2))
currNode = 0
print(kthLargestElem(t, 3))
currNode = 0
print(kthLargestElem(t, 4))
currNode = 0
print(kthLargestElem(t, 5))
currNode = 0
print(kthLargestElem(t, 6))
currNode = 0
print(kthLargestElem(t, 7))
currNode = 0
print(kthLargestElem(t, 8))
