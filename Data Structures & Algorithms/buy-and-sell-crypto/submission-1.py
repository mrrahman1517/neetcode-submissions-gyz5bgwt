class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        res = 0
        for right in range(1, n):
            while prices[left] > prices[right]:
                left += 1
            res = max (res, prices[right] - prices[left])
        return res