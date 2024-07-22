class Solution:
    def countSubstrings(self, s, t):
        n, m = len(s), len(t)

        match = [[0 for _ in range(m+1)] for _ in range(n+1)]
        matchone = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    match[i][j] = 1 + match[i-1][j-1]
                    matchone[i][j] = matchone[i-1][j-1]
                else:
                    match[i][j] = 0
                    matchone[i][j] = 1 + match[i-1][j-1]

        return sum([sum(i) for i in matchone])


        
        