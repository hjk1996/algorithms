# tag: greedy
# description
'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        count = 0
        # while right most index is not reached
        while r < len(nums)-1:
            # find the right farthest index that can be reached from l to r
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, nums[i]+i)

            # update l and r    
            # it is guaranteed that you can always reach the last index   
            l=r+1
            r=farthest
            count+=1
        
        return count