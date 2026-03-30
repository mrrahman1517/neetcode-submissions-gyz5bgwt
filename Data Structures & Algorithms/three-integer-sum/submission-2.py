class Solution:

    def twoSum(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        res = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        return res
        

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array in time O(nlogn)
        nums = sorted(nums)
        nset = set()
        output = []
        for i, num in enumerate(nums):
            if num not in nset:
                nset.add(num)
                presults = self.twoSum(nums[i+1:], -num)
                if presults:
                    for presult in presults:
                        entry = [num] + presult
                        output.append(entry)
        return output