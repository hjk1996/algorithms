# two pointer, sliding window, queue
# description
'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.

You can only see the k numbers in the window. 

Each time the sliding window moves right by one position.

Return the max sliding window.
'''

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # stores the indices of the elements in the window
        res = []
        # l and r are the left and right indices of the window
        l = r = 0

        while r < len(nums):
            # if the current element is greater than the last element in the queue, 
            # pop the last element in the queue while the current element is greater than the last element in the queue
            # because, In that case, the last element in the queue will never be the max element in the window
            # so, first item in the queue will be the max element in the window
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # append the current right index to the queue
            q.append(r)

            # if the left index is out of the window, pop the left index from the queue
            if q[0] < l:
                q.popleft()
            
            # if the window size is equal to k, append the max element in the window to the result
            # and increment the left index to move the window to the right
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1

            # increment the right index to move the window to the right
            r += 1
        
        
        
        return res