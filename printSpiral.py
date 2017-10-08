"""
Given an M x N array, print it in spiral order.
"""
def printSpiral(arr):
    if len(arr) == 0:
        return
    left, right = 0, len(arr[0])-1
    top, bottom = 0, len(arr)-1
    while left < right or top < bottom:
        if top <= bottom:
            for a in range(left, right+1):
                print(arr[top][a])
            top += 1
        if left <= right:
            for a in range(top, bottom+1):
                print(arr[a][right])
            right -= 1
        if top <= bottom:
            for a in range(right, left-1, -1):
                print(arr[bottom][a])
            bottom -= 1
        if left <= right:
            for a in range(bottom, top-1, -1):
                print(arr[a][left])
            left += 1
# Print nothing
printSpiral([[]])
# Print 1, 2, 3, 4, 5
printSpiral([[1, 2, 3, 4, 5]])
# Print 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
printSpiral([[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20]])
