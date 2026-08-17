class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = len(board)
        C = len(board[0])

        # check rows
        for r in range(R):
            s = set()

            for c in range(C):
                if board[r][c] == ".":
                    continue

                if board[r][c] in s:
                    return False

                s.add(board[r][c])

        # check columns
        for c in range(C):
            s = set()

            for r in range(R):
                if board[r][c] == ".":
                    continue

                if board[r][c] in s:
                    return False

                s.add(board[r][c])

        # check 3 x 3 boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):

                s = set()

                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):

                        if board[r][c] == ".":
                            continue

                        if board[r][c] in s:
                            return False

                        s.add(board[r][c])

        return True