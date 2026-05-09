class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose the matrix (swap rows and columns)
        for i in range(n):
            for j in range(i + 1, n):      # start from i+1 to avoid double swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row (to make it clockwise)
        for row in matrix:
            row.reverse()
