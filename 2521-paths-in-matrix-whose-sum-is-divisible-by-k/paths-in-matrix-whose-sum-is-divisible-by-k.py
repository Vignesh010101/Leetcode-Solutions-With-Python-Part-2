class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0][grid[0][0] % k] = 1
        
        mod = 10 ** 9 + 7
        
        for x in range(0, n):
            for y in range(0, m):
                for q in range(k):
                    if x + 1 < n:
                        dp[x + 1][y][(q + grid[x + 1][y]) % k] += dp[x][y][q]
                        dp[x + 1][y][(q + grid[x + 1][y]) % k] %= mod
                    if y + 1 < m:
                        dp[x][y + 1][(q + grid[x][y + 1]) % k] += dp[x][y][q]
                        dp[x][y + 1][(q + grid[x][y + 1]) % k] %= mod
        
        return dp[n - 1][m - 1][0]