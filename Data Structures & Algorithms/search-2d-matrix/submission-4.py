class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowr = 0
        highr = len(matrix) - 1
        correctrow = -1

        while lowr <= highr:
            midr = (lowr+highr)//2
            if(matrix[midr][len(matrix[midr]) - 1] < target):
                lowr = midr + 1
            elif(matrix[midr][len(matrix[midr]) - 1] >= target and matrix[midr][0] <= target):
                correctrow = midr
                break
            else:
                highr = midr-1
        
        if correctrow == -1:
            return False





        low = 0
        high = len(matrix[correctrow]) - 1
        while low <= high:
            mid = (high + low)//2
            if matrix[correctrow][mid] == target:
                return True
            elif matrix[correctrow][mid] < target:
                low = mid+1
            else:
                high = mid-1

        return False