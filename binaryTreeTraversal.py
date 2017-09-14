from collections import deque
"""
Prints all values in the binary tree level by level, from left to right.
"""
def solution(node):
    queue = deque([])
    queue.append(node)
    while len(queue) > 0:
        node = queue.popleft()
        if node == None:
            continue
        print(node.val)
        queue.append(node.left)
        queue.append(node.right)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# Should print 4, 21, 3, 100, 41, -1, -2
root = Node(4)
root.right = Node(3)
root.right.right = Node(-1)
root.right.right.left = Node(-2)
root.left = Node(21)
root.left.right = Node(41)
root.left.left = Node(100)
solution(root)
