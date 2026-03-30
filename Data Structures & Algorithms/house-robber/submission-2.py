class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        r = [0] * n
        r[0] = nums[0]
        r[1] = max(r[0], nums[1])
        for i in range(2, n):
            r[i] = max(r[i - 1], nums[i] + r[i - 2])
        return r[n - 1]