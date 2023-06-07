# data structure: heap
# description
'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

'''


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stones to negative values to make it a max heap
        stones = [(-w, w) for w in stones]
        # heapify the stones
        heapq.heapify(stones)
        # while there are more than 1 stone left
        while len(stones) > 1:
            # the heaviest stone
            first = heapq.heappop(stones)
            # the second heaviest stone
            second = heapq.heappop(stones)
            # if the stones are not the same, add the difference to the heap
            if first[1]-second[1]>0:
                heapq.heappush(stones, (-first[1]+second[1],first[1]-second[1]))
            
        # if there are no stones left, return 0
        # else, return the last stone
        if not stones:
            return 0
        else:
            return stones[0][1]