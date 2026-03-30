class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 0;
        int len = prices.size();
        int maxProfit = 0;
        while (r < len) {
            if (prices[l] < prices[r]) {
                maxProfit = max(maxProfit, prices[r] - prices[l]);
            }
            else { // prices[l] >= prices[r]
                l = r;
            }
            r++;
        }
        return maxProfit;
    }
};
