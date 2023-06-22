# tag: dfs, graph, backtracking, hashset
# description
'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, 
and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''

# my solution (backtracking)
# accepted, but it was slow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])
        visited = set()
        res = set()

        def dfs(r, c, prev):
            # base cases
            # if all oceans are reachable, no need to search further
            if all(oceans):
                return
            # if current cell is visited, return
            if (r, c) in visited:
                return
            # if current cell is out of range, mark the corresponding ocean as reachable
            if r < 0 or c < 0:
                oceans[0] = True
                return 
            if r >= height or c >= width:
                oceans[1] = True
                return 
            # if current cell is higher than previous cell, return
            if heights[r][c] > prev:
                return
            # if current cell is already in res, mark all oceans as reachable and return
            if (r, c) in res:
                oceans[0] = True
                oceans[1] = True
                return  

            # bakctracking
            visited.add((r,c))
            dfs(r+1, c, heights[r][c])
            dfs(r-1, c, heights[r][c])
            dfs(r, c+1, heights[r][c])
            dfs(r, c-1, heights[r][c])
            visited.remove((r,c))

        for r in range(height):
            for c in range(width):
                oceans = [False, False]
                dfs(r, c, heights[r][c])
                if all(oceans):
                    res.add((r, c))

        return [list(r) for r in res]

# better solution (dfs)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        # dfs from all cells on the border
        # border to center
        def dfs(r, c, visited, prevHeight):
            # base cases
            if r < 0 or r >= height or c < 0 or c >= width or (r,c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # start dfs from border cells
        for r in range(height):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, width-1, atlantic, heights[r][width-1])
        for c in range(width):
            dfs(0, c, pacific, heights[0][c])
            dfs(height-1, c, atlantic, heights[height-1][c])
        
        # find cells that are reachable from both oceans
        for r in range(height):
            for c in range(width):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        

        return res
