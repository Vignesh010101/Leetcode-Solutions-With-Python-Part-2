class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 1_000_000_007 
        
        @cache 
        def fn(n, k): 
            """Return number of possible text of n repeated k times."""
            if n < 0: return 0
            if n == 0: return 1
            ans = 0
            for x in range(1, k+1): ans = (ans + fn(n-x, k)) % MOD
            return ans 
        
        ans = 1
        for key, grp in groupby(pressedKeys): 
            if key in "79": k = 4
            else: k = 3
            ans = (ans * fn(len(list(grp)), k)) % MOD 
        return ans 