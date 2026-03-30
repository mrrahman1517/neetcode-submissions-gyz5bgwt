class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int l = 0;
       unordered_set<char> duplicate;
       int maxSubString = 0;
       for (int r = 0; r < s.length(); r++) {
            while (duplicate.find(s[r]) != duplicate.end()) {
                duplicate.erase(s[l]);
                l++;
            }
            duplicate.insert(s[r]);
            // at this point no duplicates
            maxSubString = max (maxSubString, r - l + 1);
       } 
       return maxSubString;
    }
};
