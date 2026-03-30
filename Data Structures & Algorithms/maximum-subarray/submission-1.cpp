class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0];
        int currMax = nums[0];
        if (nums.size() == 1) {
            return nums[0];
        }
        for (int i = 1; i < nums.size(); i++) {
            if (currMax < 0) {
                currMax = 0;
            }
            currMax += nums[i];
            if (currMax > maxSub) {
                maxSub = currMax;
            }
        }
        return maxSub;
    }
};
