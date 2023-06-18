# tag: greedy, sliding window
# description
'''
You are given a string s. 
We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts. 

(it just means that we need to make partitions as many as possible, and words appear in one partition should not appear in other partitions)
'''

# my solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        # count the number of each character
        counter = {}        
        for c in s:
            counter[c] = 1 + counter.get(c, 0)

        # use sliding window to find the partition
        l = r = 0
        # words in the current window
        temp = set()
        while r < len(s):
            # add the word to the current window
            temp.add(s[r])
            # discount the number of the word in the counter
            counter[s[r]] -= 1      
            canPartition=True
            for c in temp:
                # if the word in the current window still exists in the counter
                # we cannot make a partition
                # because the word would appear in other partitions in that case
                if counter[c] != 0:
                    canPartition = False
                    break
            
            # if we can make a partition
            if canPartition:
                # add the length of the partition to the result
                res.append(r-l+1)
                # move the left pointer to the right
                l=r+1
                # clear the current window
                temp = set()
            
            # move the right pointer to the right
            r+=1
        
        return res