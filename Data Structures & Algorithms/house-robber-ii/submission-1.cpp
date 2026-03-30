class Solution {
public:

    int rob_linear(vector<int>& nums) {
        int n = nums.size();
        int dp[n];
        dp[0] = nums[0];
        dp[1] = max(nums[1], nums[0]);
        for (int i = 2; i < n; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[n-1];
    }

    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        vector<int> part1;
        for (int i = 0; i < nums.size() - 1; i++) {
            part1.push_back(nums[i]);
        }    
        int max1 = rob_linear(part1);

        vector<int> part2;
        for (int i = 1; i < nums.size(); i++) {
            part2.push_back(nums[i]);
        }
        int max2 = rob_linear(part2);
        return max(max1, max2);
    }
};
