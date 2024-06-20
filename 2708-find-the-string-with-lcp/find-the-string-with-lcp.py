class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = []
        for i in range(n): 
            tabu = set()
            for j in range(i): 
                if lcp[i][j]: 
                    ans.append(ans[j])
                    break
                else: tabu.add(ans[j])
            else: 
                for ch in ascii_lowercase: 
                    if ch not in tabu: 
                        ans.append(ch)
                        break
                else: return ""
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1): 
            for j in range(n-1, -1, -1): 
                if ans[i] == ans[j]: 
                    if i == n-1 or j == n-1: dp[i][j] = 1
                    else: dp[i][j] = 1 + dp[i+1][j+1]
                if dp[i][j] != lcp[i][j]: return ""
        return "".join(ans)