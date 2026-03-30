class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # idea DP
        # sort by start value
        # store first interval, and its end value
        # for each new interval, test for overlap
        # if overlap, delete interval with max end value, update max end value
        # greedy so local decisions should be optimal
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x[0])
        endmax = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            # if overlap
            if intervals[i][0] >= endmax:  
                # no overlap, update max endpoint  
                endmax = max(endmax, intervals[i][1])
            else:
                # overlap, ignore interval with greater endpoint
                count += 1
                endmax = min(endmax, intervals[i][1])
        return count
        