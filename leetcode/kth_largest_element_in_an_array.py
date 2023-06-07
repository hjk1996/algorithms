#type: sort, recursion

#description
'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k-th largest element is in the (n-k)th index of the sorted array
        k = len(nums) - k
        # quick sort
        # every value to the left of the pivot is smaller than the pivot
        # every value to the right of the pivot is larger than the pivot
        def quickSort(l, r, k):
            # value to compare
            pivot = nums[r]
            partitionIndex = l
            for i in range(l, r):
                # rearrange the array so that all elements less than the pivot are to the left of the pivot 
                # and all elements greater than the pivot are to the right of the pivot
                if nums[i] <= pivot:
                    nums[i], nums[partitionIndex] = nums[partitionIndex], nums[i]
                    partitionIndex += 1
            # swap the pivot with the element at the partition index
            nums[partitionIndex], nums[r] = nums[r], nums[partitionIndex]

            # if partitionIndex is smaller than k, then the k-th largest element is in the right subarray
            if partitionIndex < k: return quickSort(partitionIndex+1, r, k)
            # if partitionIndex is larger than k, then the k-th largest element is in the left subarray
            elif partitionIndex > k: return quickSort(l, partitionIndex-1, k)
            # if partitionIndex is equal to k, then the k-th largest element is the pivot
            else: return nums[partitionIndex]
        
        return quickSort(0, len(nums)-1, k)