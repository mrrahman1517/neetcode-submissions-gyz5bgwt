class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [0] * n
        dp[n - 1] = 1
        gmax = 0
        for i in range(n-2, -1, -1):
            #print(i)
            dp[i] = 1
            dpmax = 0
            for j in range(i + 1, n, 1):
                print(i, j)
                if nums[i] < nums[j]:
                    dpmax = max(dpmax, dp[j])
            dp[i] += dpmax
            gmax = max(gmax, dp[i])
        print(dp)
        return gmax
        