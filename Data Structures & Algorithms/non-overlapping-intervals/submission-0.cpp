class Solution {
public:

    //bool compareIntervals(const vector<int> &i1, const vector<int> &i2) {
    //    return i1[1] < i2[1];
    //}
    
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // sort the intervals by finish time
        sort(intervals.begin(), intervals.end(), [this](const vector<int> &i1, const vector<int> &i2) {
            return i1[1] < i2[1];
        });
        int maxCount = 0;
        //vector<int> S = intervals[0];
        maxCount++;
        int f = intervals[0][1];
        for (auto& interval: intervals) {
            if (interval[0] < f) {
                continue;
            }
            // else it does not overlap and update f
            f = interval[1];
            maxCount++;
        }
        return intervals.size() - maxCount;
    }
};
