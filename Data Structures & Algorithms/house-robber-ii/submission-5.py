class Solution:
    def rob1(self, nums):
        prev1 = 0
        prev2 = 0
        for n in nums:
            curr = max(prev1, n + prev2)
            prev2 = prev1
            prev1 = curr
        return prev1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
