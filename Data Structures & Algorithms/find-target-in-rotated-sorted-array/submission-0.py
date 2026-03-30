class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if target != nums[0] else 0
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # left half sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m -1
                else:
                    l = m + 1
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1