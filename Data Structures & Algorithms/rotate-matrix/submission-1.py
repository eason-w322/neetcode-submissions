class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row - 1):
            for j in range(i+1, col):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(row):
            matrix[i] = matrix[i][::-1]
        
        
