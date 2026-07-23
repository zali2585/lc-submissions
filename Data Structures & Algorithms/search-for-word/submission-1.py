class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            if not(0 <= row < len(board) and 0 <= col < len(board[0])):
                return False
            if board[row][col] != word[i]:
                return False
            
            board[row][col] = '#'

            found = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )
            board[row][col] = word[i]
            return found
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (dfs(row, col, 0)):
                    return True
        return False
"""

"""

            