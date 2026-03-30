class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        vector<int> result;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (hashtable.count(diff)) {
                return {hashtable[diff], i};
            }
            hashtable[nums[i]] = i;
        }
    }
};
