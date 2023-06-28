# tag: stack
# description
'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 

If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        stack = []
        ans = [0 for _ in range(len(temps))]
        for i, t in enumerate(temps):
            # if current temperature is greater than the temperature at the top of the stack
            while stack and stack[-1][-1] < t:
                j, t2 = stack.pop()
                # update ans[j] to the number of days we have to wait to get a warmer temperature
                ans[j] = i-j
            # append current temperature and its index to the stack
            stack.append((i, t))
        return ans


                