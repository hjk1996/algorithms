# data structure: heap
# description
'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums
        # minHeap 생성
        heapq.heapify(self.nums)
        # heap에 k개의 숫자만 저장 (minHeap이므로 가장 큰 k개의 숫자만 남음)
        while len(nums) > k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        # 힙 업데이트
        heapq.heappush(self.nums, val)
        # 힙 사이즈가 k보다 커졌다면 pop
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # 힙의 가장 작은 값이 k번째로 큰 값
        return self.nums[0]