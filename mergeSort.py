"""
Performs merge sort on the given array in NLog(N) time.
"""
def merge(arr):
    mid = len(arr) / 2
    if mid > 0:
        left = merge(arr[0:mid])
        right = merge(arr[mid:len(arr)])
        arr = sort(left, right)
    return arr

# Helper function to combine two sorted arrays into one sorted array.
def sort(left, right):
    newArr = []
    leftPointer = 0
    rightPointer = 0
    while leftPointer < len(left) and rightPointer < len(right):
        if left[leftPointer] <= right[rightPointer]:
            newArr.append(left[leftPointer])
            leftPointer += 1
        else:
            newArr.append(right[rightPointer])
            rightPointer += 1
    if leftPointer < len(left):
        newArr = newArr + left[leftPointer:]
    if rightPointer < len(right):
        newArr = newArr + right[rightPointer:]
    return newArr


print(merge([5,4,3,2,1]))
print(merge([]))
print(merge([16,1,734,12,899,102,11,3,12,-54]))
print(merge([2]))
