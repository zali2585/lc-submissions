class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        
        def dfs(row, col):
            if not(0 <= row < rows and 0 <= col < cols):
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in dirs:
                dfs(row + dr, col + dc)

        for row in range (rows):
            for col in range (cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands

