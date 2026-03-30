class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int a = nums[i];
            if (i > 0 and nums[i-1] == a) {
                continue;
            }
            int left = i+1;
            int right = n-1;
            while (left < right) {
                int sum = a + nums[left] + nums[right];
                if (sum < 0) {
                    left++;
                }
                else if (sum > 0) {
                    right--;
                }
                else {
                    result.push_back({a, nums[left], nums[right]});
                    left++;
                    while (nums[left] == nums[left-1] && left < right) {
                        left++;
                    }
                    right--;
                    while (nums[right] == nums[right+1] && left < right) {
                        right--;
                    }
                }
            }
        }
        return result;
    }
};
