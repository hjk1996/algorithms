# tag: trie
# description
'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
'''

#my first solution (it didn't work because of time limit exceeded)
#i used dfs to search all possible words in the board
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        HEIGHT = len(board)
        WIDTH = len(board[0])
        res = []
        def dfs(r, c, i, word, path):
            if i == len(word):
                return True
            
            if (r, c) in path:
                return False
            
            if r < 0 or r >= HEIGHT or c < 0 or c >= WIDTH:
                return False

            if board[r][c] != word[i]:
                return False
            
            
            path.add((r, c))
            res1 = dfs(r+1, c, i+1, word, path)
            res2 = dfs(r, c+1, i+1, word, path)
            res3 = dfs(r-1, c, i+1, word, path)
            res4 = dfs(r, c-1, i+1, word, path)
            path.remove((r, c))

            return (res1 or res2 or res3 or res4)
        
        for word in words:
            exist = False
            for r in range(HEIGHT):
                if exist:
                     break
                for c in range(WIDTH):
                    path = set()
                    exist = dfs(r, c, 0, word, path)
                    if exist:
                        res.append(word)
                        break
        
        return res



