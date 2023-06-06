# two pointer
# description
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n1 + n2 + n3 = 0 
        # sort array to use two pointer
        nums = sorted(nums)
        res = []

        for i, n in enumerate(nums):
            # to avoid duplicate combinations, skip if n is same as previous n
            if i > 0 and n == nums[i-1]:
                continue
            
            # two pointer to find n2 and n3
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    # to avoid duplicate combinations, skip if nums[l] is same as previous (nums[l-1])
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        
        return res