# tag: grpah, dfs
# description
'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

# my first solution (dfs)
# searching regions that are surrounded by 'X'
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        height = len(board)
        width = len(board[0])
   
        def dfs(r, c, visited):
            # base cases
            # if current cell is water or visited, return
            if (r, c) in visited:
                return True
            # if current cell is out of range, all four directions are not surrounded by 'X'
            # so return False
            if r < 0 or r >= height or c < 0 or c >= width:
                return False
            # if current cell is 'X', return True
            if board[r][c] == "X":
                return True

            visited.add((r,c))
            down = dfs(r+1, c, visited)
            up = dfs(r-1, c, visited)
            right = dfs(r, c+1, visited)
            left = dfs(r, c-1, visited)
            # if any of down, up, right, left is False, return False
            return down and up and right and left
            
          

        for r in range(height):
            for c in range(width):
                # if current cell is 'O', do DFS
                if board[r][c] == "O":
                    visited = set()
                    # if the region is surrounded by 'X', flip all 'O's to 'X's
                    res = dfs(r, c, visited)
                    if res:
                        for y, x in visited:
                            board[y][x] = "X"

#my second solution (dfs)
# searching regions that are not surrounded by 'X'
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        height = len(board)
        width = len(board[0])
        # set of visited cells
        # it only contains cells that are not surrounded by 'X'
        visited = set()

        def dfs(r, c):
            # base cases
            # if current cell is out of range, or
            # if current cell is visited, or
            # if current cell is 'X', end recursion
            if r < 0 or r >= height or c < 0 or c >= width or (r,c) in visited or board[r][c] == "X":
                return
            
            # recursive cases
            # mark current cell as visited
            visited.add((r,c))
            # search all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
  
        # search all four edges
        for r in range(height):
            dfs(r, 0)
            dfs(r, width-1)
        for c in range(width):
            dfs(0, c)
            dfs(height-1, c)

        # flip all regions that are surrounded by 'X'
        for r in range(height):
            for c in range(width):
                if (r, c) not in visited:
                    board[r][c] = "X"                 