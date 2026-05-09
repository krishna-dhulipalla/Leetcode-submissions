class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        def capture(r, c):
            if r < 0 or c < 0 or r == ROW or c == COL or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for dr, dc in directions:
                capture(r+dr, c+dc)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r in (0, ROW - 1) or c in (0, COL - 1)):
                    capture(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
