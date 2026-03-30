class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        left = 0
        right = n - 1
        res = (right - left) * min(heights[left], heights[right])
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
            res = max(res, (right - left) * min(heights[left], heights[right]))
        return res