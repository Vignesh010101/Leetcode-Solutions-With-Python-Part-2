class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        d, ans, n = defaultdict(lambda:[-1,-1]), [], len(s)
        for j in range(min(32,n)):
            for i in range(n-j):
                num = int(s[i:i+j+1], 2)
                if num not in d: d[num] = [i, i+j]
        return [d[a^b] for a, b in queries]
