class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(row, col, i):
            if i == len(word):
                return True
            if not(0 <= row < rows and 0 <= col < cols):
                return False
            if board[row][col] != word[i]:
                return False
            
            original = board[row][col]
            board[row][col] = '#'

            dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in dirs:
                if (dfs(row + dr, col + dc, i + 1)):
                    return True

            board[row][col] = original

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (dfs(row, col, 0)):
                    return True
        return False
"""
MAIN IDEA:
you want to test every elem in board as the starting letter of word. if only that start letter is matched, you start recursing from that point to up down left right of board to try and find next letter
think of base cases: what means word is found? what means that the curr spot of board is invalid
-> invalid if.... 1.) off of board or 2.) not equal to word[i] 
if u pass both those then u know the letter ur looking at is in the word at the right pos
so u mark the spot as used, then recurse from all nearby spots looking for word[i + 1]
-> if all those fail, or at any point in the recursion stack it fails, you come back and check curr letter from marked bc its no longer part of any path that spells word
return found, which represents if any of those directions are successful which with recursion, will only come back true at top layer if entire word is found


"""

            