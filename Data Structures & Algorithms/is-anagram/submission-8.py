class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s and t are anagrams, they will have ths same frequency distributions
        # find the letter count of s and store in a hashmap
        # then iterate through letters in t and compare
        if len(s) != len(t):
            return False
        fmap = defaultdict(int)
        for ch in s:
            fmap[ch] += 1
        
        for ch in t:
            if fmap[ch] > 0:
                fmap[ch] -= 1
            else:
                return False
        return True