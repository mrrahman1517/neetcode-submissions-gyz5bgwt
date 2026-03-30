class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # sort based on first index
        intervals.sort(key = lambda x: x[0])
        output = []
        output.append(intervals[0])
        for i in range(1, len(intervals)):
            right = output[-1]
            # if overlap
            if right[1] >= intervals[i][0]: 
                #merge
                right[1] = max(right[1], intervals[i][1])
            else:
                output.append(intervals[i])    
        return output
        