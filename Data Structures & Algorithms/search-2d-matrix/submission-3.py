class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if(matrix[row][len(matrix[row]) - 1] < target):
                continue
            low = 0
            high = len(matrix[row])
            while low <= high: # simply apply a binary search once we've isolated the row that contains the value
                mid = (high + low)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    low = mid+1
                else:
                    high = mid-1

        return False