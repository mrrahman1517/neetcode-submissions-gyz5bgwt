class Solution {
public:

    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> f(26);
        for (int i = 0; i < s.size(); i++) { 
            f[s[i]-97]++;
            f[t[i]-97]--;
        } 
        for (int i = 0; i < 26; i++) {
            if (f[i] != 0) 
                return false;
        }
        return true;
    }
};
