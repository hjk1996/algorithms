# tag: array
# description
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # prefix and postfix
        l, r = 1, 1
        for i in range(len(nums)):
            res[i] *= l
            l = l*nums[i]
            res[-1-i] *= r
            r = r*nums[-1-i]
        
        return res