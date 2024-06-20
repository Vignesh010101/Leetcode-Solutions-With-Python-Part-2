class Solution:
    def z_function(self, s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        z[0] = len(s)
        return z

    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s, idx = [''] * n, 0
        for i in range(n):
            if i + lcp[i][i] != n: return ''
            if s[i] == '':
                if idx > 25: return ''
                s[i] = chr(ord('a') + idx)
                idx += 1
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]: return ''
                if lcp[i][j]:
                    if s[j] != '' and s[j] != s[i]: return ''
                    s[j] = s[i]
        s = ''.join(s)
        return '' if any(self.z_function(s[i:]) != lcp[i][i:] for i in range(n)) else s