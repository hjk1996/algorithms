# tag: two pointer
# description
'''
Given a string s, return the longest palindromic substring in s.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0

        for i in range(len(s)):
            # when the length of the palindrome is odd
            l, r = i, i
            # expand the palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                l -= 1
                r += 1
            
            # when the length of the palindrome is even
            l, r = i, i+1
            # expand the palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                l -= 1
                r += 1
                
        return res
