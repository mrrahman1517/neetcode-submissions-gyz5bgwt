class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[l] < nums[m], min = nums[l]
        # if nums[l] > nums[m], min in left half
        # if nums[m] > nums[h], min in right half
        if len(nums) == 1:
            return nums[0]
        # all unique elements means the min should exist and is unique
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l) // 2
            print(m)
            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[l] > nums[m]:
                r = m
            elif nums[m] >= nums[r]:
                l = m + 1    
        