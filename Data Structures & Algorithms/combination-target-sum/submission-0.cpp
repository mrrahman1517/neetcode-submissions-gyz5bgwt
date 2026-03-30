class Solution {
public:

    vector<int> currComb;
    vector<vector<int>> result;

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        dfs(0, target, nums);
        return result;
    }

    void dfs(int index, int target, vector<int>& nums) {

        if (target == 0) {
            result.push_back(currComb);
            return;
        }
        if (index >= nums.size() or target < 0) {
            return;
        }
        currComb.push_back(nums[index]);
        dfs(index, target - nums[index], nums);
        currComb.pop_back();
        dfs(index + 1, target, nums);
    }
};
