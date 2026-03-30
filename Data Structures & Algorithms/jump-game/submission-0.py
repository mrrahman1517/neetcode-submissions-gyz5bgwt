class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            print(i)
            for d in range(nums[i] + 1):
                print(i, d)
                dp[i] = dp[i] or dp[i + d]
                print(dp[i])
        return dp[0]