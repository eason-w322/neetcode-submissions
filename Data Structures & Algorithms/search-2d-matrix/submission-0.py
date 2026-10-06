class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        target_index = -1
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                target_index = mid
                break
            elif matrix[mid][-1] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
        if target_index == -1:
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[target_index][mid] == target:
                return True
            elif matrix[target_index][mid] < target:
                left = mid + 1
            elif matrix[target_index][mid] > target:
                right = mid - 1
        return False
        

        
