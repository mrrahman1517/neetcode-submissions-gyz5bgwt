class Solution {
public:
    int climbStairs(int n) {
        // F(n) = F(n-1) + F(n-2)
        // base case
        if (n == 1) {
            return 1;
        }
        vector<int> F(n+1);
        F[0] = 1;
        F[1] = 1;
        for (int i = 2; i <= n; i++) {
            F[i] = F[i-1] + F[i-2];
        }
        return F[n];
    }
};
