class Solution:
    def minimumScore(self, s: str, t: str) -> int:

        m, n =  len(s), len(t)
        suff, j = [0]*m, n

        for i in range(m)[::-1]:

            if j > 0 and s[i] == t[j-1]: j -= 1
            suff[i] = j-1

        ans, j = j, 0

        for i in range(m):

            ans = min(ans, max(0, suff[i] - j + 1))
            if j < n and s[i] == t[j]: j += 1

        return min(ans, n-j)