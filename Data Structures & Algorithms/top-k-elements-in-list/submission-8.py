class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track frequencies with counter object
        #create an array with index as frequencies 
        # for each frequency create a list of elements of said frequency
        # read of from max available frequency
        # min frequency = 1, max freq = size of array, so the array is bounded
        fmap  = Counter(nums)
        maxf = max(fmap.values())
        buckets = [[] for _ in range(maxf + 1)]
        result = []
        for val, count in fmap.items():
            buckets[count].append(val)
        print(buckets)
        i = 0
        for count in range(maxf, 0, -1):
            if buckets[count]:
                for val in buckets[count]:
                    result.append(val)
                    i += 1
                    if i == k:
                        return result
        return result
        