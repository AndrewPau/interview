"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.
"""
def canPartition(nums):
    total = 0
    for num in nums:
        total += num
    # If the total sum is odd, we can't partition into two equal subsets.
    if total % 2 == 1:
        return False
    vals = set()
    vals.add(total/2)
    # On each iteration, we subtract all values we've seen by the current number.
    # This represents finding all possible combinations.
    for num in nums:
        nextVals = []
        for val in vals:
            nextVal = val - num
            # If at any time you reach 0, you've found one subset.
            # Thus, the remaining numbers must equal the other subset.
            if nextVal == 0:
                return True
            nextVals.append(nextVal)
        # Add after iteration to avoid changing the set size
        for val in nextVals:
            vals.add(val)
    return False

# True, False, True
print(canPartition([1, 5, 11, 5]))
print(canPartition([1, 2, 3, 5]))
print(canPartition([1, 4, 7, 2, 9, 3]))
