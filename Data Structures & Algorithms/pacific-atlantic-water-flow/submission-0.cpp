class Solution {
public:
    int rows;
    int cols;
    vector<vector<bool>> pacific;
    vector<vector<bool>> atlantic;

    vector<vector<int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};

    bool valid(const int r, const int c) {
        return r >= 0 && r < rows && c >= 0 && c < cols;
    }

    void dfs_pacific(const vector<vector<int>>& heights, const int r, const int c) {
        pacific[r][c] = true;
        for (auto& dir: dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (valid(nr, nc) && !pacific[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                dfs_pacific(heights, nr, nc);
            }
        }
    } 

    void dfs_atlantic(const vector<vector<int>>& heights, const int r, const int c) {
        atlantic[r][c] = true;
        for (auto& dir: dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (valid(nr, nc) && !atlantic[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                dfs_atlantic(heights, nr, nc);
            }
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty()) {
            return {};
        }
        rows = heights.size();
        cols = heights[0].size();

        pacific = vector<vector<bool>>(rows);
        atlantic = vector<vector<bool>>(rows);
        for (int i = 0; i < rows; i++) {
            pacific[i] = vector<bool>(cols, false);
            atlantic[i] = vector<bool>(cols, false);
        }

        for (int i = 0; i < rows; i++) {
            dfs_pacific(heights, i, 0);
            dfs_atlantic(heights, i, cols - 1);
        }

        for (int j = 0; j < cols; j++) {
            dfs_pacific(heights, 0, j);
            dfs_atlantic(heights, rows - 1, j);
        }

        vector<vector<int>> result;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.push_back({r, c});
                }
            }
        }
        return result;
    }
};
