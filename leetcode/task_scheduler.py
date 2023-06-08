# tag: heap, queue
# description
'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.
'''

import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the number of each task
        taskCounter = {}
        for t in tasks:
            taskCounter[t] = 1 + taskCounter.get(t, 0)

        # create a max heap of the task counts
        taskHeap = [v for v in taskCounter.values()]
        heapq.heapify(taskHeap)

        # create a queue to store the tasks that are in the cooldown period
        coolQ = deque()
        time = 0

        while taskHeap or coolQ:
            # if the cool time of the first item in the queue passed, push it back to the heap
            if coolQ and coolQ[0][1] < time:
                c, t = coolQ.popleft()
                heapq.heappush(taskHeap, c)
            
            # if there is a task in the heap, pop it and push it to the queue
            if taskHeap:
                tc = heapq.heappop(taskHeap)
                if tc+1 != 0:
                    coolQ.append((tc+1, time+n))

            # increment the time
            time += 1


        return time
            