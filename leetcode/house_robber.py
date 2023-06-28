# tag: dp
# description
'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

# my solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        
        if len(nums) == 2:
            return max(nums)
        
        # dp[i] = max amount of money that can be robbed from 0 to i-th house
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # if we rob i-th house, we cannot rob (i-1)-th house
            # if we rob (i-1)-th house, we cannot rob i-th house
            # so we take the max of these two cases
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        

        return dp[-1]