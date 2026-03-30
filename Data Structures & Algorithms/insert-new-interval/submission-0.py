class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(intervals)):
            # first case, new interval to the left of the current ith interval
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                output += intervals[i:]
                return output
            elif newInterval[0] > intervals[i][1]: # new interval completely to the right of ith interval, append all upto ith
                output.append(intervals[i])
            else:
                # overlap with current, so merge
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        output.append(newInterval)
        return output
        