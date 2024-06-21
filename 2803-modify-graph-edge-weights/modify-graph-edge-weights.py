class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = [[0]*n for _ in range(n)]
        for u, v, w in edges: graph[u][v] = graph[v][u] = w
        orig = [inf] * n
        orig[source] = 0 
        pq = [(0, source)]
        while pq: 
            d, u = heappop(pq)
            if d == orig[u]: 
                for v, w in enumerate(graph[u]): 
                    if w and w != -1 and d+w < orig[v]: 
                        orig[v] = d+w
                        heappush(pq, (orig[v], v))
        if orig[destination] < target: return []
        if orig[destination] == target: 
            ans = []
            for u, v, w in edges: 
                if w == -1: w = 2_000_000_000
                ans.append([u, v, w])
            return ans 
        dist = [inf] * n
        dist[source] = 0 
        parent = [-1] * n 
        pq = [(0, source)]
        while pq: 
            d, u = heappop(pq)
            if u == destination: break 
            if d == dist[u]: 
                for v, w in enumerate(graph[u]): 
                    if w: 
                        if w == -1: dd = d+1
                        else: dd = d+w
                        if dd < dist[v]: 
                            dist[v] = dd 
                            parent[v] = u 
                            heappush(pq, (dd, v))
        if d > target: return []
        while u >= 0: 
            p = parent[u]
            if p >= 0: 
                if graph[p][u] == -1: 
                    if orig[p] < target: 
                        graph[p][u] = graph[u][p] = target - orig[p]
                        break 
                    graph[p][u] = graph[u][p] = 1 
                target -= graph[u][p]
            u = p 
        ans = []
        for u, v, w in edges: 
            if graph[u][v] == -1: graph[u][v] = 2_000_000_000
            ans.append([u, v, graph[u][v]])
        return ans