class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                # nums[m] cant be min, start m+1
                l = m + 1
            else:
                # rotate in left half
                r = m
        return nums[l]