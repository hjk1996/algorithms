# tag: dfs, graph
# description
'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

# my solution (dfs)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        height = len(grid)
        width = len(grid[0])
        visited = set()
        stack = []

        dys = [1, -1, 0, 0]
        dxs = [0, 0, 1, -1]
        for r in range(height):
            for c in range(width):
                # if current cell is land and not visited, do DFS
                if grid[r][c] == 1 and (r,c) not in visited:
                    # initialize area
                    area = 0
                    stack.append((r,c))
                    visited.add((r, c))
                    while stack:
                        r, c = stack.pop()
                        # increment area
                        area += 1
                        for i in range(4):
                            dy, dx = dys[i], dxs[i]
                            nr, nc = r + dy, c + dx
                            if nr >= 0 and nr < height and nc >= 0 and nc < width:
                                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                                    visited.add((nr, nc))
                                    stack.append((nr, nc))
                    # update maxArea             
                    maxArea = max(maxArea, area)
        
        return maxArea

# recursive dfs solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        height, width = len(grid), len(grid[0])
        def dfs(r, c):
            # base case
            # if r or c is out of range, or current cell is water(or visited), return 0
            if r < 0 or r >= height or c < 0 or c>= width or grid[r][c] == 0:
                return 0
            
            # recursive case
            # mark current cell as visited by setting it to 0
            grid[r][c] = 0
            # search all four directions
            down = dfs(r+1, c)
            up = dfs(r-1, c)
            right = dfs(r, c+1)
            left = dfs(r, c-1)
            # return 1 + sum of areas of all four directions
            return 1 + down + up + right + left

        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea