class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = matrix[mid // cols][mid % cols]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1
        return False