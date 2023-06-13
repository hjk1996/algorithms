# tag: dynamic programming, greedy
# description
'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''



# My Solution: dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = max(nums[i], dp[i-1]+nums[i])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxValue = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            # update maxValue
            maxValue = max(maxValue, dp[i])
        
        return maxValue

# Other Solution: greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum+nums[i])
            maxSum = max(maxSum, curSum)
        
        return maxSum