class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        if(n == 1) {
            return 1;
        }
        vector<vector<bool>> dp(n, vector<bool>(n, 0));
        //init
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        int count = n;
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    if (len == 2) {
                        dp[i][j] = true;
                    }
                    else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                if (dp[i][j]) {
                    count++;
                }
            }    
        }
        return count;
    }
};
