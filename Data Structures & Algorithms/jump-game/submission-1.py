class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for d in range(nums[i] + 1):
                dp[i] = dp[i] or dp[i + d]
        return dp[0]