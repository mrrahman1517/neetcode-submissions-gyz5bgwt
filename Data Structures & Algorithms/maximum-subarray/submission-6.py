class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window??
        rsum = 0
        res = nums[0]
        for num in nums:
            rsum += num
            res = max(res, rsum)
            if rsum < 0:
                rsum = 0
        return res 
        