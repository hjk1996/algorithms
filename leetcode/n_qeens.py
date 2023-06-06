class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cs = set()
        # pds = positive diagonal indices (row + col)
        pds = set()
        # nds = negative diagonal indices (row - col)
        nds = set()
        board = [["."]*n for _ in range(n)]

        def dfs(r):
            #base case
            # when row index is equal to n 
            # (we have reached the end of the board and placed all queens)
            if r == n:
                copy = ["".join(r) for r in board]
                ans.append(copy)
                return
                
            for c in range(n):
                # if c is in cs or r-c is in nds or r+c is in pds
                if c in cs or r-c in nds or r+c in pds:
                    continue
                    # skip to next iteration


                cs.add(c)
                nds.add(r-c)
                pds.add(r+c)
                board[r][c] = "Q"
                dfs(r+1)
                # clean up
                cs.remove(c)
                nds.remove(r-c)
                pds.remove(r+c)
                board[r][c] = "."
    

        dfs(0)

        return ans