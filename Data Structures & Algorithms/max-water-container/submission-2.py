class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        left = 0
        right = n - 1
        res = 0        
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            area = w * h
            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return res