class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dset = set()
        left = 0
        n = len(s)
        maxl = 0
        for right in range(n):
            while left <= right and s[right] in dset:
                # keep removing from left
                dset.remove(s[left])
                left += 1
            dset.add(s[right])
            maxl = max(maxl, right - left + 1)
        return maxl
        