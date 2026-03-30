class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap
        # for each number check if target - num is in the map
        # then keep adding to map
        smap = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in smap:
                return [smap[target - num], i]
            smap[num] = i
        return []
        