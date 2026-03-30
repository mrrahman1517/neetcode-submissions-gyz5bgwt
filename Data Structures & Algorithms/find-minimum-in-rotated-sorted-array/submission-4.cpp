class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        int left = 0;
        int right = nums.size() - 1;
        int result = 10000;
        
        while (left <= right) {
            
            int mid = (left+right)/2;
            if (nums[mid] < result)
                result = nums[mid];
            if (nums[left] < nums[right]) {
                if (nums[left] < result) {
                    result = nums[left];
                }    
            }
                
            if(nums[mid] >= nums[left]) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return result;
    }
};
