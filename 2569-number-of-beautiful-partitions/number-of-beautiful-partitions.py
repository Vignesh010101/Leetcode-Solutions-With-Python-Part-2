class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9 + 7

        def isPrime(c):
            return c in ['2', '3', '5', '7']

        @lru_cache(None)
        def dp(i, k):
            if k == 0 and i <= n:
                return 1
            if i >= n:
                return 0

            ans = dp(i+1, k)  # Skip
            if isPrime(s[i]) and not isPrime(s[i-1]):  # Split
                ans += dp(i+minLength, k-1)
            return ans % MOD

        if not isPrime(s[0]) or isPrime(s[-1]): return 0

        return dp(minLength, k-1)