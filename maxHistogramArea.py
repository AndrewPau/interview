"""
Given an array of heights, find the maximum rectangular area of the array.
"""
def maxArea(array):
    stack = []
    maxArea = 0
    for index in range(len(array)):
        # If it's empty or you have a larger element, add it.
        if len(stack) == 0 or stack[-1][1] <= array[index]:
            stack.append((index, array[index]))
        # You have an increasing stack so that when you find a smaller element,
        # the next area is the top of the element and everything to the right until your current index.
        else:
            # If you remove a larger number, your number inherits its start position
            # If I remove a 4 and add a 3, the sum of my 3's starts where the 4 started.
            lastIndex = index
            while len(stack) > 0 and stack[-1][1] > array[index]:
                val = stack.pop()
                lastIndex = val[0]
                area = val[1] * (index - val[0])
                if area > maxArea:
                    maxArea = area
            stack.append((lastIndex, array[index]))
    # Empty the rest of the stack
    while len(stack) > 0:
        val = stack.pop()
        area = val[1] * (len(array) - val[0])
        if area > maxArea:
            maxArea = area
    return maxArea

# Should print 9, 4, 5, 12
print(maxArea([1,2,3,4,5]))
print(maxArea([1,2,5]))
print(maxArea([2,1,2,3,1]))
print(maxArea([2,3,2,3,2,3]))
