# tag: greedy
# description
'''
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # rightmost index that can be reached
        r = 0
        for i in range(len(nums)):
            # if i-th index is reachable
            if i<=r:
                # update r
                r=max(r, i+nums[i]) 
                # if the last index is reachable, return True
                if len(nums)-1 <= r:
                    return True
        # if the last index is not reachable, return False
        return False

