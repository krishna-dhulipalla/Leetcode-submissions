class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols - 1]:
                left, right = 0, cols - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
