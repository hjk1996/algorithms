# tags: dp
# description
'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

# my solution
class Solution:
    # there could be two cases
    # 1. rob the first house
    # 2. rob the last house
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = [0]*2  + nums[1:]
        nums2 = [0]*2 + nums[:-1]
        dp1 = [0 for _ in range(len(nums1))]
        dp2 = [0 for _ in range(len(nums2))]

        for i in range(2, len(nums1)):
            dp1[i] = max(nums1[i]+dp1[i-2], dp1[i-1])
        
        for i in range(2, len(nums2)):
            dp2[i] = max(nums2[i]+dp2[i-2], dp2[i-1])
        
        return max(dp1[-1],dp2[-1])

# other solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        # compare the case of rob the first house and the case of rob the last house
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2