class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxf = max(freq.values())
        #print(maxf)
        buckets = [[] for _ in range(maxf + 1)]
        for n, c in freq.items():
            buckets[c].append(n)
        #print(buckets) 
        out = []
        for count in range(maxf, 0, -1):
            if buckets[count]:
                for val in buckets[count]:
                    out.append(val)
                    if len(out) == k:
                        return out
        return []
        