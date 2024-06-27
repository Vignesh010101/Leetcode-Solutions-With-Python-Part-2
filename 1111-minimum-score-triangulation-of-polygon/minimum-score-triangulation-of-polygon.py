#Recursive
#Time Complexity: Exponential
#Space Complexity: O(n)
class Solution1:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def solve(i, j):
            if i+1 == j:
                return 0
            m = float('inf')
            for k in range(i+1, j):
                m = min(m, values[i] * (values[j]*values[k]) + solve(i, k) + solve(k, j))
            return m
        return solve(0, len(values)-1)
    
#Memoization (Top-Down)
#Time Complexity: O(n^2)
#Space Complexity: O(n^2) + O(n)
class Solution2:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def solve(i, j):
            if i+1 == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            m = float('inf')
            for k in range(i+1, j):
                m = min(m, values[i] * (values[j]*values[k]) + solve(i, k) + solve(k, j))
            dp[i][j] = m
            return dp[i][j]
        
        n = len(values)
        dp = [[-1 for j in range(n)] for i in range(n)]
        return solve(0, n-1)

#Tabulation (Bottom-Up)
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                m = float('inf')
                for k in range(i+1, j):
                    m = min(m, values[i]*values[j]*values[k] + dp[i][k] + dp[k][j])
                dp[i][j] = m
        return dp[0][n-1]