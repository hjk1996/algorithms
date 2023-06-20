# tag: stack, greedy, dp
# description
'''

'''


# stack solution
class Solution:
    
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []

        for i in range(len(s)):
            p = s[i]
            # if it is open parenthesis, push it to openStack
            if p == "(":
                openStack.append(i)
            # if it is star, push it to starStack
            elif p == "*":
                starStack.append(i)
            # if it is close parenthesis, pop openStack first, if it is empty, pop starStack, if it is empty too, return False
            else:
                if openStack:
                    openStack.pop()
                    continue
                
                if starStack:
                    starStack.pop()
                    continue
                
                return False
        
    
        while openStack:
            # if openStack is not empty and starStack is empty, return False
            if not starStack:
                return False
            
            # if both openStack and starStack are not empty,
            # and the last index of openStack is smaller than the last index of starStack,
            # pop both stacks
            if openStack[-1] < starStack[-1]:
                openStack.pop()
                starStack.pop()
            # if the last index of openStack is greater than the last index of starStack,
            # return False
            else:
                return False
        
        # if openStack is empty, return True
        return True

# greedy solution
class Solution:
    
    def checkValidString(self, s: str) -> bool:
        # leftMin: the minimum number of open parenthesis
        # leftMax: the maximum number of open parenthesis
        leftMin, leftMax = 0, 0 
        for p in s:
            # if it is open parenthesis, increment both leftMin and leftMax
            if p == "(":
                leftMin += 1
                leftMax += 1
            # if it is close parenthesis, decrement both leftMin and leftMax
            elif p == ")":
                leftMin -= 1
                leftMax -= 1
            # if it is star, increment leftMax and decrement leftMin
            else:
                leftMin -= 1
                leftMax += 1
            
            # if leftMax is smaller than 0, return False
            # because it means that there are more close parenthesis than open parenthesis
            if leftMax < 0:
                return False
            
            # if leftMin is smaller than 0, set it to 0 
            if leftMin < 0:
                leftMin = 0
        
        # if leftMin is 0, return True
        return leftMin == 0


# dp solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def walk(i, l):
            # base cases
            # if index is greater or equal to the length of the string, 
            # return True if left parenthesis count is 0, otherwise return False
            if i >= len(s):
                return l == 0
            
            
            # if current charactor is "*", there are three cases:
            if s[i] == '*':
                # 1. "*" is an open parenthesis
                if walk(i+1, l+1):
                    return True
                # 2. "*" is a close parenthesis
                if l > 0 and walk(i+1, l-1):
                    return True
                # 3. "*" is an empty string
                if walk(i+1, l):
                    return True
            # if current charactor is an open parenthesis, increment left parenthesis count and move to next index
            elif s[i] == '(':
                return walk(i+1, l+1)
            # if current charactor is a close parenthesis, and left parenthesis count is greater than 0,
            #  decrement left parenthesis count and move to next index
            else:
                return l > 0 and walk(i+1, l-1)

        return walk(0, 0)



