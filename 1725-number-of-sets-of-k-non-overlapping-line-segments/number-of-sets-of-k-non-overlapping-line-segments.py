import sys
sys.setrecursionlimit(10**9)

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        M = 10**9+7
        
        @lru_cache(None)
        def helper(idx, rem, isInMiddle):
            if idx==n-1:
                if rem:
                    return 0
                else:
                    return 1
            ans = 0
            if isInMiddle:
                ans += helper(idx+1, rem, isInMiddle)
                ans %= M
                ans += helper(idx+1, rem, not isInMiddle)
                ans %= M
                if rem>0:
                    ans += helper(idx+1, rem-1, isInMiddle)
                    ans %= M
            else:
                ans += helper(idx+1, rem, isInMiddle)
                ans %= M
                if rem>0:
                    ans += helper(idx+1, rem-1, not isInMiddle)
                    ans %= M
            return ans
        return helper(0, k, False)
    