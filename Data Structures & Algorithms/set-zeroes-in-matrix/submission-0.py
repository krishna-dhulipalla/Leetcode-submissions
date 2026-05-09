class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowZero = False
        colZero = False

        for r in range(row):
            if matrix[r][0] == 0:
                colZero = True
        for c in range(col):
            if matrix[0][c] == 0:
                rowZero = True
        
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, row):
            if matrix[r][0] == 0:
                for i in range(1, col):
                    matrix[r][i] = 0
        for c in range(1, col):
            if matrix[0][c] == 0:
                for i in range(1, row):
                    matrix[i][c] = 0
        if rowZero:
            for c in range(col):
                matrix[0][c] = 0    # zero first row
        if colZero:
            for r in range(row):
                matrix[r][0] = 0