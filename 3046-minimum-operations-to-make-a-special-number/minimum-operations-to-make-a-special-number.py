class Solution:
    def minimumOperations(self, num: str) -> int:
        ans = inf 
        for p in "00", "25", "50", "75": 
            cand = 0 
            i = 1
            for ch in reversed(num): 
                if p[i] == ch: i -= 1
                else: cand += 1
                if i == -1: break 
            else: continue 
            ans = min(ans, cand)
        return ans if ans < inf else len(num) - int('0' in num)