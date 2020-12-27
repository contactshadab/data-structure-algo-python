'''
https://leetcode.com/problems/merge-intervals/
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''


# Run time complexity: O(n log n) for sorting
# Space complexity: O(log N), recursive stack for in-pace sorting
# Intuition: If we sort intervals by start time we'll have all intervals starting together or after previous one in continuous slot
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        previous = res[-1]
        current = intervals[i]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            res.append(current)

    return res


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
