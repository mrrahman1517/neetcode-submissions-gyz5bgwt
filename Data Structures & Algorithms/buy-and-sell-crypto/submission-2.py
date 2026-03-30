class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        res = 0
        for right in range(left + 1, n):
            if prices[left] > prices[right]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])
        return res