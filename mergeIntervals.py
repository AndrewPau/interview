"""
Given a list of intervals in the form of [start, end], merge the overlapping intervals.
"""
def merge(intervals):
    intervals = sorted(intervals, key=lambda interval: interval[0])
    mergedIntervals = []
    for interval in intervals:
        if len(mergedIntervals) == 0 or mergedIntervals[-1][1] < interval[0]:
            mergedIntervals.append(interval)
        elif mergedIntervals[-1][1] >= interval[1]:
            continue
        else:
            mergedIntervals[-1][1] = interval[1]
    return mergedIntervals

# Print [[1,2], [3,12]] and [[0,9], [10,12], [13,20]]
a = [[1,2], [3,7], [5,12], [9,12]]
b = [[1,5], [0,9], [16, 20], [10,12], [13,17]]
print(merge(a))
print(merge(b))
