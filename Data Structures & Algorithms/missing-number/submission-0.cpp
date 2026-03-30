class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int sum = n*(n+1)/2;
        int x = 0;
        for (auto& num: nums) {
            x += num;
        }
        return sum - x;
    }
};
