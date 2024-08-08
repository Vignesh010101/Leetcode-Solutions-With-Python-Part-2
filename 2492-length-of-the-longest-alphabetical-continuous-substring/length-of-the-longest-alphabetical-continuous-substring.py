class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first, max_len = 0,0

        for i in range(1, len(s) + 1):
            if s[first:i] in alphabet:
                max_len = max(max_len, i - first)
            else:
                first = i - 1
        return max_len