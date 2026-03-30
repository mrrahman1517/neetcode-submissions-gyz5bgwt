class Solution {
public:
    vector<int> parent;
    vector<int> size;
    int count;
    
    bool merge(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        if (pu == pv) {
            return false;
        }
        if (size[pu] < size[pv]) {
            parent[pu] = pv;
            size[pv] += size[pu];
        }
        else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
        if (count > 1) {
            count--;
        }
        return true;
    }

    int find(int u) {
        while(parent[u] != u) {
            u = parent[u];
        }
        return u;
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        count = n;
        parent = vector<int>(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        size = vector<int>(n, 1);
        for (auto& edge: edges) {
            if(!merge(edge[0], edge[1])) {
                return false;
            }
        }
        return count == 1;
    }
};
