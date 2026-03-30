class Solution {
public:
    vector<bool> visited;
    vector<vector<int>> graph;

    void dfs(int u) {
        visited[u] = true;
        for (auto& v: graph[u]) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return 1;
        }
        graph.resize(n);
        //visited = vector<bool>(n);
        visited.resize(n, false);
        for (int i = 0; i < n; i++) {
            graph[i] = vector<int>(n);
        }
        for (auto& edge: edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if(!visited[i]) {
                dfs(i);
                count++;
            }
        }
        return count;
    }
};
