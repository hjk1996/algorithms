# tag: dfs, backtracking
# description
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
'''



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

    
        HEIGHT = len(board)
        WIDTH = len(board[0])
        # path stores the coordinates that have been visited
        path = set()
        def dfs(cur, r, c):
            # if the coordinate is already in the path, return False
            if (r, c) in path:
                return False
            
            # if the coordinate is out of the range of the board, return False
            if r < 0 or r >= HEIGHT or c < 0 or c >= WIDTH:
                return False
            
            # if the character at the coordinate is not the same as the current character in word, return False
            if board[r][c] != word[cur]:
                return False

            # after all, if the cursor is at the end of the word, return True
            if cur == len(word)-1:
                return True

            # otherwise, add the coordinate to the path, and recursively check the four directions
            path.add((r, c))
            res1 = dfs(cur+1, r+1, c)
            res2 = dfs(cur+1, r-1, c)
            res3 = dfs(cur+1, r, c+1)
            res4 = dfs(cur+1, r, c-1)
            # clean up the path
            path.remove((r, c))
            # return True if any of the four directions is True
            return (res1 or res2 or res3 or res4)
        

        # iterate through the board, and check if the word exists
        for r in range(HEIGHT):
            for c in range(WIDTH):
                if dfs(0, r, c):
                    return True


        return False