class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxRectangle = 0;
        int l = 0;
        int r = heights.size() - 1;
        maxRectangle = (r-l) * min(heights[l], heights[r]);
        while (l < r) {
            if (heights[l] <= heights[r]) {
                l++;
            }
            else {
                r--;
            }
            maxRectangle = max(maxRectangle, (r-l) * min(heights[l], heights[r]));
        }
        return maxRectangle;
    }
};
