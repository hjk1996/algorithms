# tag: graph, dfs
# description
'''
'''

# my solution (dfs)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        route = {i: list() for i in range(numCourses)}
        for c, p in prerequisites:
            route[c].append(p)
        finished = set()
        visited = set()

        def dfs(c):
            # base cases
            # if there is a cycle in the route, return False
            if c in visited:
                return False
            # if prerequisites are all met, return True
            if not route[c]:
                # add course to res if it is not in res
                if c not in finished:
                    res.append(c)
                    finished.add(c)
                return True
            # recursive cases
            visited.add(c)
            for crs in route[c]:
                # if there is a cycle in the route, return False
                if not dfs(crs):
                    return False
            # empty course's route since all prerequisites are met
            route[c] = list()
            # add course to res
            res.append(c)
            finished.add(c)
            # remove course from visited for backtracking
            visited.remove(c)
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res