class Solution:
    def maxRepOpt1(self, s: str) -> int:
        pos = defaultdict(lambda: [inf, -inf])
        for i,c in enumerate(s):
            pos[c] = [min(pos[c][0], i), max(pos[c][1], i)] # min and max char pos in s
        freq = defaultdict(int)
        max_len = 1
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            while len(freq) > 2 or len(freq) == 2 and min(freq.values()) > 1: # if violates statement #1
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]] # clean up the freq counter.... also could be Counter() :/
                left += 1
            max_char = max(freq.keys(), key=lambda x: freq[x]) # find max freq element
            max_len = max(max_len, freq[max_char] + (pos[max_char][0] < left or right < pos[max_char][1])) # statement #2
        return max_len