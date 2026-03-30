class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;
        vector<vector<string>> result;
        for (auto& str: strs) {
            string sorted = str;
            sort(sorted.begin(), sorted.end());
            group[sorted].push_back(str);
        }
        for (auto& [key, value]: group) {
            result.push_back(value);
        }
        return result;
    }
};
