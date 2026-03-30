class Solution:

    # invariant decode(encode(s)) == s
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        # idea, create a string with each string and prepend length
        # then we can decode uniquely
        for s in strs:
            encoded_string += str(len(s))
            encoded_string += "#"
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0
        n = len(s)
        while index < n:
            j = index
            while s[j] != "#":
                j += 1
            len1 = int(s[index:j])
            index = j + 1
            # now we read of len1 chars
            curr = s[index : index + len1]
            decoded_strings.append(curr)
            index += len1
        return decoded_strings