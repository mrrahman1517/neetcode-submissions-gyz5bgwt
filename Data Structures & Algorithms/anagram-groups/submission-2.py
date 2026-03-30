class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for any string, use the sorted string as a key and then add all values for the same key
        group = defaultdict(list)
        for str in strs:
            group["".join(sorted(str))].append(str)

        return list(group.values())