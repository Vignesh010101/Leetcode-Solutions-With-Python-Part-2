class Solution:
    def platesBetweenCandles(self, s: str, qs: List[List[int]]) -> List[int]:
        n = len(s)
        prefcandle = [-1] * n
        suffcandle = [0] * n
        pref = [0] * n

        ind = -1
        c = 0
        for i in range(n):
            if ind != -1 and s[i] == '*':
                c += 1
            elif s[i] == '|':
                ind = i
            pref[i] = c

        ind = -1
        for i in range(n):
            if s[i] == '|':
                ind = i
            prefcandle[i] = ind

        ind = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                ind = i
            suffcandle[i] = ind

        m = len(qs)
        ans = [0] * m

        for i in range(m):
            c = 0
            l = qs[i][0]
            r = qs[i][1]

            if prefcandle[r] < l or suffcandle[l] > r:
                continue

            ans[i] = pref[prefcandle[r]] - pref[suffcandle[l]]
        return ans
