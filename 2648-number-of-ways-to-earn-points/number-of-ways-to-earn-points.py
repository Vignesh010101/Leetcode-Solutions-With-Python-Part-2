class Solution:
    def waysToReachTarget(self, T, A):
        dp = [1] + [0] * T
        mod = 10 ** 9 + 7
        for c, m in A:
            for i in range(m, T + 1):
                dp[i] += dp[i - m]
            for i in range(T, (c + 1) * m - 1, -1):
                dp[i] = (dp[i] - dp[i - (c + 1) * m]) % mod
        return dp[-1] % mod