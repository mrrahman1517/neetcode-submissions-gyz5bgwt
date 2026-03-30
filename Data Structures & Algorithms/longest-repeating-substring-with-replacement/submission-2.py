class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        fmap = {chr(i):0 for i in range(65, 65 + 26)}
        left = 0
        wmax = 0
        for right in range(n):
            fmap[s[right]] += 1
            fmax = max(fmap.values())
            while right - left + 1  - fmax > k:
                fmap[s[left]] -= 1
                left += 1
            wmax = max(wmax, right - left + 1)
        return wmax
        