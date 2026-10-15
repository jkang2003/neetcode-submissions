class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = set()
        for row in range(9):
            for col in range(9):
                if board[row][col] in rowset and board[row][col] != ".":
                    return False
                else:
                    rowset.add(board[row][col])
            rowset.clear()
        
        colset = set()
        for col in range(9):
            for row in range(9):
                if board[row][col] in colset and board[row][col] != ".":
                    return False
                else:
                    colset.add(board[row][col])
            colset.clear()
        
        cells = {(0,0) : set(), (0,1) : set(), (0,2) : set(), (1,0) : set(), (1,1) : set(), (1,2) : set(), (2,0) : set(), (2,1) : set(), (2,2) : set()}
        for row in range(9):
            for col in range(9):
                cell = (row//3, col//3)
                if board[row][col] in cells[cell] and board[row][col] != ".":
                    return False
                else:
                    cells[cell].add(board[row][col])

        return True