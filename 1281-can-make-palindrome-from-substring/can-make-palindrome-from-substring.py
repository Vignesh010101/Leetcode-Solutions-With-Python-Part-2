class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        trans = {k: v for v, k in enumerate(set(s))}

        dp = [[0] * len(trans)]
        for ch in s:
            dp.append(dp[-1][:])
            dp[-1][trans[ch]] += 1
        
        ans = []
        for start, end, k in queries:
            sm = sum((a - b) % 2 for a, b in zip(dp[end + 1], dp[start]))
            ans.append(sm // 2 <= k) 
        return ans