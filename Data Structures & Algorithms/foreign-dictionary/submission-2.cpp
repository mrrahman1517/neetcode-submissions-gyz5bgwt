class Solution {
public:
    string foreignDictionary(vector<string>& words) {
        if (words.size() == 1) {
            return "abcdefghijklmnopqrstuvwxyz";
        }

        // create graph

        unordered_map<char, vector<char>> graph;
        unordered_map<char, int> indeg;
        for (auto& word: words) {
            for (auto& c: word) {
                graph[c] = vector<char>();
                indeg[c] = 0;
            }
        }
        int n = words.size();
        for (int i = 0; i < n - 1; i++) {
            if (words[i].size() > words[i+1].size() && words[i].rfind(words[i+1], 0) == 0) {
                return "";
            }
            else {
                // find first no equal chars
                size_t c;
                for (c = 0; c < words[i].size() && c < words[i+1].size(); c++) {
                    if (words[i][c] != words[i+1][c]) {
                        graph[words[i][c]].push_back(words[i+1][c]);
                        indeg[words[i+1][c]]++;
                        break;
                    }   
                }
            }
        }

        // the DAG is created
        queue<char> q;
        for (auto& deg: indeg) {
            if (deg.second == 0) {
                q.push(deg.first);
            }
        } 
        if (q.empty()) {
            return "";
        }
        string toporder;
        while (!q.empty()) {
            char c = q.front();
            q.pop();
            toporder += c;
            for (auto& neighbor: graph[c]) {
                indeg[neighbor]--;
                if (indeg[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        if (toporder.size() != indeg.size()) {
            return "";
        }
        return toporder;
    }
};
