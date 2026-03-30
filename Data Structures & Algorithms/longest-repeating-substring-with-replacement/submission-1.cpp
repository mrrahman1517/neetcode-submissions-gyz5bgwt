class Solution {
public:

    int maxElement(const map<char, int>& fmap) {
        int maxValue = 0;
        for (auto it = fmap.begin(); it != fmap.end(); it++) {
            if (it->second > maxValue) {
                maxValue = it->second;
            }
        }
        return maxValue;
    }

    int characterReplacement(string s, int k) {
       int l = 0;
       int res = 0;
       map<char, int> freq;
       for (int r = 0; r < s.length(); r++) {
            freq[s[r]]++;
            while (r-l+1 - maxElement(freq) > k) {
                if (freq[s[l]] > 0) {
                    freq[s[l]]--;
                }
                l++;
            }
            // at this point the window is valid
            res = max(res, r-l+1);
       } 
       return res;
    }
};
