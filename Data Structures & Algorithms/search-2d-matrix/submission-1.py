class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] < target:
                    continue
                elif matrix[row][col] > target:
                    return False
                else:
                    return True

        return False