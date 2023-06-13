# tag: min heap, max heap
# description
'''
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''


import heapq

class MedianFinder:

    def __init__(self):
        # left half of the array is stored in maxHeap
        self.leftHeap = [] 
        # right half of the array is stored in minHeap
        self.rightHeap = [] 
        

    def addNum(self, num: int) -> None:
        # add num to the leftHeap if its length is smaller than the rightHeap
        if len(self.leftHeap) < len(self.rightHeap):
            heapq.heappush(self.leftHeap, -num)
        else:
            heapq.heappush(self.rightHeap, num)
        
        # validate the heaps
        # if values exist in both heaps
        if self.leftHeap and self.rightHeap:
            # if the top of the leftHeap is greater than the top of the rightHeap, swap them
            if -self.leftHeap[0] > self.rightHeap[0]:
                leftValue = heapq.heappop(self.leftHeap)
                rightValue = heapq.heappop(self.rightHeap)
                heapq.heappush(self.leftHeap, -rightValue)                
                heapq.heappush(self.rightHeap, -leftValue)                
        

    def findMedian(self) -> float:
        # if the total length of the array is even, return the average of the top of the leftHeap and the top of the rightHeap
        if (len(self.leftHeap) + len(self.rightHeap)) % 2 == 0:
            return (-self.leftHeap[0] + self.rightHeap[0])/2
        # if the total length of the array is odd, return the top of the rightHeap
        else:
            return self.rightHeap[0]
                