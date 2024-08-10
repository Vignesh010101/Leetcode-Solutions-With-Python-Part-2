class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for _ in range(len(roads)+1)]
        for u, v in roads: 
            graph[u].append(v)
            graph[v].append(u)
        
        ans = 0 
        def dfs(u, p): 
            """Return number of people going through city u."""
            nonlocal ans 
            ppl = 0 
            for v in graph[u]: 
                if v != p: ppl += dfs(v, u)
            ppl += 1
            if u: ans += (ppl + seats - 1) // seats
            return ppl 
        
        dfs(0, -1)
        return ans 