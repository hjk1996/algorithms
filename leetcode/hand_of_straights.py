# tag: heap, greedy
# description
'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, 
and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, 
return true if she can rearrange the cards, or false otherwise.
'''

# my first solution
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) is not divisible by groupSize, return False
        if len(hand) % groupSize != 0:
            return False
        
        # sort hand
        hand = sorted(hand)


        # while hand is not empty
        while hand:
            # find the smallest number in hand
            cur = hand[0]-1

            for i in range(groupSize):
                # if consecutive number is in hand, increment cur and continue
                if cur+1 in hand:
                    cur += 1
                # if consecutive number is not in hand, return False
                else:
                    return False
                
            # remove consecutive numbers from hand
            for i in range(groupSize):
                hand.remove(cur)
                cur -= 1

        # if the process above is completed without returning False, return True
        return True

# my second solution
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) is not divisible by groupSize, return False
        if len(hand) % groupSize != 0:
            return False

        # count the number of each card
        counter = {}
        for n in hand:
            counter[n] = 1 + counter.get(n, 0)
        
        # create a min heap
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        # while minHeap is not empty
        while minHeap:
            # temporary list to store numbers that the counter is greater than 0
            temp = []
            # find the smallest number in minHeap
            cur = minHeap[0]-1

            for _ in range(groupSize):
                # if minHeap is empty, return False, because there is no consecutive number
                if not minHeap:
                    return False
                # pop the smallest number from minHeap to compare with cur
                num = heapq.heappop(minHeap)
                # if the difference between num and cur is not 1, then it is not consecutive, so return False
                if num- cur != 1:
                    return False
                # if the difference between num and cur is 1, then it is consecutive
                else:
                    # decrement the counter of num
                    counter[num] -= 1
                    # if the counter of num is greater than 0, append num to temp
                    if counter[num] > 0:
                        temp.append(num)
                    # update cur
                    cur = num
            
            # append numbers in temp to minHeap
            if temp:
                for num in temp:
                    heapq.heappush(minHeap, num)
        
        # if the process above is completed without returning False, return True
        return True