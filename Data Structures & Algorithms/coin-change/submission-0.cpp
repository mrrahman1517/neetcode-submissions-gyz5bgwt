class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> opt(amount+1, 100000);
        opt[0] = 0;
        for (int i = 1; i <= amount; i++) {
            int minValue = 100000;
            for (auto& coin: coins) {
                if (i - coin >= 0) {
                    minValue = min(minValue, opt[i-coin] + 1);
                }
            }
            opt[i] = minValue;
        }
        return opt[amount] == 100000 ? -1: opt[amount];
    }
};
