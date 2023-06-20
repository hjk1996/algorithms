# tag: graph, bfs, dfs
# description
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''


# my solution (dfs)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        HEIGHT = len(grid)
        WIDTH = len(grid[0])
        visited = [[0]*WIDTH for _ in range(HEIGHT)]
        

        def dfs(r, c):
            # base cases
            # if r or c is out of range, return
            if r < 0 or r >= HEIGHT or c < 0 or c >= WIDTH:
                return
            # if current cell is water or visited, return
            if grid[r][c] == "0" or visited[r][c]:
                return
            
            # recursive cases
            # mark current cell as visited
            visited[r][c] = 1
            # search all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(HEIGHT):
            for c in range(WIDTH):
                # if current cell is land and not visited, do DFS
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    count += 1 

        return count