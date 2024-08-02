class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        count = 0
        ans1 = 0
        ans2 = 0
        for i in range(len(text)-1, -1, -1):
            if text[i] == pattern[0]:
                ans1 += count + 1
                ans2 += count
            if text[i] == pattern[1]:
                count += 1
        return max(ans1, ans2 + count)