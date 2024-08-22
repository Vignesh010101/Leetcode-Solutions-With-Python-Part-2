class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        groups = [[] for _ in range(n)]
        for start, end, gold in offers:
            groups[end].append((start, gold))
        
        f = [0] * (n+1) # initialize it as 0
        for end, x in enumerate(groups):
            f[end+1] = f[end]
            for start, gold in x: # iterate the bill which ends at the index i
                f[end+1] = max(f[end+1], f[start] + gold)
        return f[n]