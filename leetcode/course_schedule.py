# tag: graph, bfs, dfs, backtracking
# description
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

# my solution (bfs)
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        noPre = set(range(numCourses))
        route = defaultdict(set)
        visited = set()
        for p in prerequisites:
            # update noPre
            if p[0] in noPre:
                noPre.remove(p[0])
            # update route
            route[p[0]].add(p[1])
        
        # noPre is the starting point
        q = deque(noPre)

        while q:
            c = q.popleft()
            visited.add(c)
            removeList = []
            for p in route:
                # if course in in the route of another course, remove it
                if c in route[p]:
                    route[p].remove(c)
                
                # if course' prerequisites are all visited, add it to q
                if not route[p]:
                    q.append(p)
                    # add it to removeList
                    removeList.append(p)
            
            # remove courses in removeList
            for p in removeList:
                del route[p]
        
        # if all courses are visited, return True
        return True if len(visited) == numCourses else False

# another solution (dfs, backtracking)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        route = {i: list() for i in range(numCourses)}

        # build route
        for c, p in prerequisites:
            route[c].append(p)
        # 
        visited = set()

        def dfs(c):
            # base cases
            # if there is a cycle in the route, return False
            if c in visited:
                return False
            # if prerequisites are all met, return True
            # empty means all prerequisites are met
            if not route[c]:
                return True
            # recursive cases
            # add course to visited
            visited.add(c)
            # do backtracking
            for p in route[c]:
                # if there is a cycle in the route, return False
                if not dfs(p):
                    return False
            # remove course from visited for backtracking
            visited.remove(c)
            # empty course's route since all prerequisites are met
            route[c] = list()
            # if all prerequisites are met, return True
            return True
        
        for i in range(numCourses):
            # if there is a cycle in the route, return False
            if not dfs(i):
                return False
        # if all courses are successfully taken, return True
        return True
            
