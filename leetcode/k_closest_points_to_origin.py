# data structure: heap
# description
'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate the distance of each point from the origin
        points_with_d = [[(p[0]**2+p[1]**2)**0.5, p[0], p[1]] for p in points]
        # create a min heap
        heapq.heapify(points_with_d)
        res = []
        # pop k points from the heap
        for _ in range(k):
            p = heapq.heappop(points_with_d)
            res.append(p[1:])

        return res 
