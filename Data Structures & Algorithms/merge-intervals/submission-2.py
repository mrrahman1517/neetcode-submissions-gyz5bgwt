class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # set disjoint union
        # if overlap, merge
        # idea 2 minheap
        # sort based on first index
        intervals.sort(key = lambda x: x[0])
        output = []
        output.append(intervals[0])
        print(output)
        for i in range(1, len(intervals)):
            #output.append(intervals[i])
            #right = output[len(output) - 1]
            right = output.pop()
            # if overlap
            if right[1] >= intervals[i][0]: 
                #merge
                output.append([min(right[0], intervals[i][0]), max(right[1], intervals[i][1])])
            else:
                output.append(right)
                output.append(intervals[i])    
            #print(output.pop())
            #print (output)
        return output
        