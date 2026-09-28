class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        grid_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set[i]:
                    return False
                row_set[i].add(board[i][j])
        
        for j in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col_set[j]:
                    return False
                col_set[j].add(board[i][j])
        
        for i in range(9):
            for j in range(i//3 * 3, (i//3 * 3) + 3):
                for k in range(i%3 * 3, i%3 * 3 + 3):
                    if board[j][k] == ".":
                        continue
                    if board[j][k] in grid_set[i]:
                        return False
                    grid_set[i].add(board[j][k])
        return True