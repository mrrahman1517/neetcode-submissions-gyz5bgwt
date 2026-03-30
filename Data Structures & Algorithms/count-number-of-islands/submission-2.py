class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            visited.add((r, c))
            if r + 1 < rows and (r + 1, c) not in visited and grid[r + 1][c] == "1":
                dfs(r + 1, c)
            if r - 1 >= 0 and (r - 1, c) not in visited and grid[r - 1][c] == "1":
                dfs(r - 1, c)
            if c + 1 < cols and (r, c + 1) not in visited and grid[r][c + 1] == "1":
                dfs(r, c + 1)
            if c - 1 >= 0 and (r, c - 1) not in visited and grid[r][c - 1] == "1":
                dfs(r, c - 1)
            

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count
