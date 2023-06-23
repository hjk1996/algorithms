# tag: graph
# description
'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

# my solution 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        height = len(grid)
        width = len(grid[0])
        rotten = set()
        dys = [1, -1, 0, 0]
        dxs = [0, 0, 1, -1]
        fresh = True
        while True:
            nextRotten = set()
            hasFresh = False
            for r in range(height):
                for c in range(width):
                    # check if there is a fresh orange
                    if grid[r][c] == 1:
                        hasFresh = True
                        continue
                    # if current cell is rotten, check if it can rot its neighbors
                    if grid[r][c] == 2 and not (r, c) in rotten:
                        rotten.add((r, c))
                        for i in range(4):
                            dy, dx = dys[i], dxs[i]
                            nextY, nextX = r + dy, c + dx
                            if nextY >= 0 and nextY < height and nextX >= 0 and nextX < width:
                                # if neighbor is fresh, rot it
                                if grid[nextY][nextX] == 1:
                                    nextRotten.add((nextY, nextX))
            
            # update grid
            for r, c in nextRotten:
                grid[r][c] = 2
            # update fresh
            fresh = hasFresh

            # if there is nothing to rot, break
            if not nextRotten:
                break
            # else, increment count
            else:
                count += 1
            
        # return -1 if there is a fresh orange, else return count
        return -1 if fresh else count