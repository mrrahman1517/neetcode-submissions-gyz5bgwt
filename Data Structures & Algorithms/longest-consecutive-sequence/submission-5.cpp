class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int maxLength = 0;
        for (auto& num: nums) {
            if (s.find(num - 1) == s.end()) {
                // num is the start of a sequence
                int length = 1;
                int item = num+1;
                while (s.find(item) != s.end()) {
                    length++;
                    item++;
                }
                maxLength = max(maxLength, length);
            }
        }
        return maxLength;
    }
};
