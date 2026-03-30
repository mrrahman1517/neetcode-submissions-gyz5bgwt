class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        window = {}
        required = len(need)
        formed = 0
        left = 0
        min_len = float('inf')
        min_start = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return "" if min_len == float('inf') else s[min_start: min_start + min_len]
        