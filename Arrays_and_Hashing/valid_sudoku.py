"""
https://leetcode.com/problems/valid-sudoku/
"""
#I made this a lot harder on myself than I needed to but it works
 
class Solution:
    
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        if not self.check_row(board): return False
        if not self.check_column(board): return False
        return self.check_grid(board)
    
    
    def check_row(self, board: list[list[str]]) -> bool:
        for row in board:
            digits = ("".join(row).replace(".", ""))
            if len(digits) != len(set(digits)): return False
        return True
    
    
    def check_column(self, board: list[list[str]]) -> bool:
        for column_index in range(0, 9):
            column_list = []
            for row_index in range(0, 9):
                cell = board[row_index][column_index]
                if cell != ".":
                    column_list.append(cell)
            #Checks if the column has duplicates
            if len(column_list) != len(set(column_list)): return False
        return True
    
    
    def check_grid(self, board: list[list[str]]) -> bool:
        grids = [[], [], []]
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                grids[j // 3].append(cell)
            if (i + 1) % 3 == 0:
                if not self.check_row(grids): return False
                grids = [[], [], []]
            
        return True