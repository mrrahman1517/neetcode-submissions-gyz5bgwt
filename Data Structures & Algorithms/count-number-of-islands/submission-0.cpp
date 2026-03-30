class Solution {
public:
    vector<vector<int>> visited;

    bool valid (int i, int j, vector<vector<char>>& grid, int n, int m) {
        return (i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == '1' and visited[i][j] == 0);
    }
    void dfs(int i, int j, vector<vector<char>>& grid, int n, int m) {
        visited[i][j] = 1;
        if (valid(i + 1, j, grid, n, m)) {
            dfs(i + 1, j, grid, n, m);
        }
        if (valid(i - 1, j, grid, n, m)) {
            dfs(i - 1, j, grid, n, m);
        }
        if (valid(i, j - 1, grid, n, m)) {
            dfs(i, j - 1, grid, n, m);
        }
        if (valid(i, j + 1, grid, n, m)) {
            dfs(i, j + 1, grid, n, m);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        visited.resize(n);
        for (int i = 0; i < n; i++) {
            visited[i] = vector<int>(m, 0);
        }
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1' and visited[i][j] == 0) {
                    count++;
                    dfs(i, j, grid, n, m);
                }
            }
        }
        return count;
    }
};
