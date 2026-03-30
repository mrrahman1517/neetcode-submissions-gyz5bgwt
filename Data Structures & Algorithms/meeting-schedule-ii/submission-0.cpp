/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int n = intervals.size();
        vector<int> start, finish;
        for (auto& interval: intervals) {
            start.push_back(interval.start);
            finish.push_back(interval.end);
        }
        sort(start.begin(), start.end());
        sort(finish.begin(), finish.end());

        int res = 0;
        int count = 0;
        int s = 0;
        int e = 0;
        while (s < n) {
            if (start[s] < finish[e]) {
                s++;
                count++;
            }
            else {
                e++;
                count--;
            }
            res = max(res, count);
        }
        return res;
    }
};
