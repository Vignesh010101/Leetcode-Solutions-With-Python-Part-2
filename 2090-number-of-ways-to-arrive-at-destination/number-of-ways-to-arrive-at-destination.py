class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for u, v, time in roads: 
            graph.setdefault(u, {})[v] = time
            graph.setdefault(v, {})[u] = time
            
        dist = [inf]*n
        dist[-1] = 0
        stack = [(n-1, 0)]
        while stack: 
            x, t = stack.pop()
            if t == dist[x]: 
                for xx in graph.get(x, {}): 
                    if t + graph[x][xx] < dist[xx]: 
                        dist[xx] = t + graph[x][xx]
                        stack.append((xx, t + graph[x][xx]))
                        
        @cache
        def fn(x):
            """Return """
            if x == n-1: return 1 
            if dist[x] == inf: return 0 
            ans = 0 
            for xx in graph.get(x, {}): 
                if graph[x][xx] + dist[xx] == dist[x]: ans += fn(xx)
            return ans % 1_000_000_007
        
        return fn(0)