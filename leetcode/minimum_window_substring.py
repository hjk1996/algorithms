# tag: sliding window, two pointers
# description
'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring  of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''


class Solution:

    def countWord(self, w):
        res = {}
        for c in w:
            res[c] = 1 + res.get(c, 0)
        return res

    # check if s contains t
    def isValid(self, s, t):
        for key in t:
            if t[key] > s.get(key, 0):
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        minWord = ""
        minLength = float("inf")
        tCount = self.countWord(t)
        sCount = {}
        # sliding window
        l = 0

        for r in range(len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            # if s[l:r+1] contains t
            while self.isValid(sCount, tCount) and l<=r:
                # update minWord
                if (r-l+1) < minLength:
                    minLength = r-l+1
                    minWord = s[l:r+1]
                # move l forward until s[l:r+1] no longer contains t
                sCount[s[l]] -= 1
                l += 1
        
        
        

        return minWord