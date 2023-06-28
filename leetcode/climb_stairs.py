#tag: dp
#description
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# recursive solution
# it is a fibonacci sequence
from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# iterative solution
class Solution:
    # number of ways to reach n-th step is equal to sum of number of ways to reach (n-1)-th step and (n-2)-th step
    # dp[i] = dp[i-1] + dp[i-2]
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1
        for i in range(n-1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        
        return n2
