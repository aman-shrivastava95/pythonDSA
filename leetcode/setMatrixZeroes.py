from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        row_zero = False
        col_zero = False

        # check if there is a zero in first row
        for r in range(R):
            if matrix[r][0] ==0:
                col_zero = True
        # check if here is a zero n first col
        for c in range(C):
            if matrix[0][c] == 0:
                row_zero = True

        #mark remaining marix leaving first row and first column, first row and col to be treated as memory to mark
        #which one col and rows need to be marked as zero
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 0:
                    #mark that row zero
                    matrix[0][j] = 0
                    #mark that column zero
                    matrix[i][0] = 0

        # mark all the column and row zeroes if that rown
        for i in range(1, R):
            for j in range(1, C):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        #check if first row and first col needs to be set zero
        if row_zero:
            for c in range(C):
                matrix[0][c] = 0

        if col_zero:
            for r in range(R):
                matrix[r][0] = 0