class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:

        g, d, ans = gcd(k,len(arr)), defaultdict(list), 0

        for i, a in enumerate(arr): d[i%g].append(a)
        for i in d: d[i].sort()
            
        return sum(d[i][-j-1]-d[i][j] for j in range((len(d[i]))//2) for i in d)
