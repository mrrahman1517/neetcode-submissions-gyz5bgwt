class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        if (n == 1) {
            return s;
        }
        int bestStart = 0;
        int bestLen = 1;
        // dp[i][j] == true  ⇔  s[i..j] is palindrome
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    if (len <= 3) {
                        dp[i][j] = true;
                    }
                    else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                else {
                    dp[i][j] = false;
                }
                if (dp[i][j] && len > bestLen) {
                    bestLen = len;
                    bestStart = i;
                }
            }
        }
        return s.substr(bestStart, bestLen);
    }
};
