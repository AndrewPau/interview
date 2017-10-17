"""
Given an array of non-negative integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
"""
def canPartitionKSubsets(nums, k):
    total = 0
    for num in nums:
        total += num
    # If the total sum is not divisible by k, it is impossible.
    if total % k != 0:
        return False
    # Initialize whether the value has been taken or not
    taken = [False for a in range(len(nums))]
    return findPartitions(total/k, taken, nums, k, 0, 0)

# Helper function that uses backtracking to find if k subsets are possible
def findPartitions(target, taken, nums, numRemaining, curr, currIndex):
    if curr == target:
        # If you've found k - 1 subsets, the last must sum to target as well.
        if numRemaining <= 1:
            return True
        # Start  the next subset
        return findPartitions(target, taken, nums, numRemaining-1, 0, 0)
    # Start at currIndex to avoid unnecessary computations.
    for a in range(currIndex, len(nums)):
        if taken[a]:
            continue
        if curr + nums[a] > target:
            continue
        taken[a] = True
        ans = findPartitions(target, taken, nums, numRemaining, curr + nums[a], a+1)
        if ans:
            return True
        # Reset the number if the subset wasn't found
        taken[a] = False
    return False

# True
print(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
