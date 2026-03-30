class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hs;
        for (auto& num: nums) {
            if (hs.find(num) != hs.end()) {
                return true;
            }
            hs.insert(num);
        }
        return false;
    }
};
