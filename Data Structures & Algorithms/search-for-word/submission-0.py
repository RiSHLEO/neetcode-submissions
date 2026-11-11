class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(index, row, col):
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if word[index] != board[row][col]:
                return False

            char = board[row][col]
            board[row][col] = "#"

            found = (backtrack(index + 1, row + 1, col) or
                     backtrack(index + 1, row - 1, col) or
                     backtrack(index + 1, row, col + 1) or
                     backtrack(index + 1, row, col - 1))
            
            board[row][col] = char
            return found

        for row in range(rows):
            for col in range(cols):
                if backtrack(0, row, col):
                    return True
        return False