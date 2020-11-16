'''
https://leetcode.com/problems/k-closest-points-to-origin/
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''

import heapq
import random


# Solution 1: Using sorting
# Run time complexity: O(nlog(n)), Space complexity: O(1)
def k_closest(points, K):
    points.sort(key=lambda point: point[0]*point[0] + point[1]*point[1])
    return points[:K]


# Solution 2: Using min heap
# Run time complexity: O(nlog(K)), Space complexity: O(K)
def k_closest_using_heap(points, K):
    heap = []
    heapq.heapify(heap)
    for point in points:
        if len(heap) < K:
            heapq.heappush(
                heap, (-1 * (point[0]*point[0] + point[1]*point[1]), point))  # Multiplying by -1 to convert it to max heap
        else:
            heapq.heappushpop(
                heap, (-1 * (point[0]*point[0] + point[1]*point[1]), point))

    return [items[1] for items in heap]


# Solution 3: Using a variant of selection sort
# Run time complexity: O(Kn), Space complexity: O(1)
def k_closest_using_selection_sort(points, K):
    def d(i): return points[i][0]*points[i][0] + points[i][1]*points[i][1]

    boundry = -1
    for k in range(K):
        smallest = boundry + 1
        for i in range(boundry+1, len(points)):
            if d(i) < d(smallest):
                smallest = i

        boundry += 1
        points[boundry], points[smallest] = points[smallest], points[boundry]

    return points[:K]


# Solution 4: Using a variant of quick sort
# Run time complexity: O(n) average, O(n^2) worst case
def k_closest_using_partition(points, K):

    def sort(points, start, end, K):
        if start >= end:
            return

        pivot = random.randint(start, end)
        points[start], points[pivot] = points[pivot], points[start]
        mid = partition(points, start, end)

        if K < mid - start + 1:
            sort(points, start, mid - 1, K)
        elif K > mid - start + 1:
            sort(points, mid+1, end, K - (mid - start + 1))

    def partition(points, start, end):
        pivot = start
        def d(i): return points[i][0] ** 2 + points[i][1] ** 2
        start += 1
        boundry = start - 1
        while start <= end:
            if d(start) < d(pivot):
                boundry += 1
                points[boundry], points[start] = points[start], points[boundry]

            start += 1

        points[boundry], points[pivot] = points[pivot], points[boundry]

        return boundry

    sort(points, 0, len(points)-1, K)

    return points[:K]


if __name__ == "__main__":
    print(k_closest([[1, 3], [-2, 2], [2, -2]], 2))
    print(k_closest_using_heap([[1, 3], [-2, 2], [2, -2]], 2))
    print(k_closest_using_selection_sort([[1, 3], [-2, 2], [2, -2]], 2))
    print(k_closest_using_partition([[1, 3], [-2, 2], [2, -2]], 2))
