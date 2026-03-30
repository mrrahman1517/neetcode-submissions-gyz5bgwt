class Solution {
public:

    set<pair<int, int>> visited;
    bool dfs(int row, int col, int idx, vector<vector<char>>& board, string word, int n, int m) {
        if (idx == word.size()) {
            return true;
        }
        if (row < 0 or row >= n or col < 0 or col >= m or board[row][col] != word[idx] or visited.count({row, col}) ) {
            return false;
        }
        bool result = false;
        visited.insert({row, col});
        result = dfs(row + 1, col, idx + 1, board, word, n, m) 
                or dfs(row - 1, col, idx + 1, board, word, n, m) 
                or dfs(row, col + 1, idx + 1, board, word, n, m)
                or dfs(row, col - 1, idx + 1, board, word, n, m);
        visited.erase({row, col});
        if (result) {
            return true;
        }
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size();
        int m = board[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dfs(i, j, 0, board, word, n, m)) {
                    return true;
                }
            }
        }
        return false;
    }
};
