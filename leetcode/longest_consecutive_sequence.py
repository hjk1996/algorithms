# Used data structure: set, list
# descriptin
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

'''

# My Solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if array is empty, return 0
        if not nums:
            return 0

        # remove duplicates and sort
        nums = sorted(set(nums))
        max_c = 1
        cur_c = 1

        # iterate through array and check if consecutive
        for i in range(len(nums)-1):
            # if consecutive, increment cur_c and update max_c
            if nums[i+1] - nums[i] == 1:
                cur_c += 1
                max_c = max(max_c, cur_c)
            # if not consecutive, reset cur_c
            else:
                cur_c = 1
        
        return max_c

# Alternative solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        max_streak = 0

        for num in num_set:
            # if num - 1 is not in num_set, then num is the start of a streak
            if num - 1 not in num_set:
                cur_num = num
                cur_streak = 1
                # while cur_num + 1 is in num_set, increment cur_num and cur_streak
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_streak += 1
                # update max_streak after each iteration
                max_streak = max(max_streak, cur_streak)
        
        return max_streak