from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]  

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()

                for h, v in directions:
                    row, col = r + h, c + v
                    if (row < 0 or row == len(grid)) or (col < 0 or col == len(grid[0])) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1
        
        return time if not fresh else -1