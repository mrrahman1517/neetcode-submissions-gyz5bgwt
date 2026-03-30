class Solution {
public:

    static bool compareIntervals(const vector<int>& i1, const vector<int>& i2) {
        return i1[0] <i2[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), compareIntervals);
        vector<vector<int>> result;
        result.push_back(intervals[0]);
        for (auto& interval: intervals) {
            // check if overlap
            if (interval[0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], interval[1]);
            }
            else {
                result.push_back(interval);
            }
        }
        return result;
    }
    
};
