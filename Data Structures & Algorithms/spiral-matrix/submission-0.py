class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        visited = set()

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                if (top, i) in visited:
                    continue
                visited.add((top, i))
                results.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                if (j, right) in visited:
                    continue
                visited.add((j, right))
                results.append(matrix[j][right])
            right -= 1

            for k in range(right, left - 1, -1):
                if (bottom, k) in visited:
                    continue
                visited.add((bottom, k))
                results.append(matrix[bottom][k])
            bottom -= 1
            
            for b in range(bottom, top - 1, -1):
                if (b, left) in visited:
                    continue
                visited.add((b, left))
                results.append(matrix[b][left])
            left += 1
        
        return results

            


            
            

        

        

