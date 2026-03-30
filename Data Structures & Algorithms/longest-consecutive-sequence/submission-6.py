class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums to a set
        # for every element check wether it is a start of a sequence by testing whether num-1 is in the set, if not move to next
        # element, otherwise it is a potential start sequence, continue checking if num++ is in the set and keep track of length

        seqTracker = set(nums)
        maxCount = 0
        for num in seqTracker:
            if num - 1 not in seqTracker:
                count = 1
                val = num + 1
                while val in seqTracker:
                    count += 1
                    val += 1
                maxCount = max(maxCount, count)
        return maxCount
        