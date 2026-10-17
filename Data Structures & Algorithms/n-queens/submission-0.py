class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        upper_diag = set()
        lower_diag = set()
        col = set()
        board = [["."] * n for _ in range(n)]
        results = []
        print(board)

        
        def backtrack(r):
            if r == n:
                results.append(["".join(i) for i in board])
                return
            
            for c in range(n):
                if c in col or (r-c) in lower_diag or (r + c) in upper_diag:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                lower_diag.add((r - c))
                upper_diag.add((r + c))
                backtrack(r + 1)
                board[r][c] = "."
                col.remove(c)
                lower_diag.remove((r - c))
                upper_diag.remove((r + c))
        
        backtrack(0)
        return results


