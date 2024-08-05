class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = val = 0 
        for i, ch in enumerate(reversed(s)): 
            if ch == '0': ans += 1
            elif i < 30 and val + (1<<i) <= k: 
                ans += 1
                val += 1<<i
        return ans 