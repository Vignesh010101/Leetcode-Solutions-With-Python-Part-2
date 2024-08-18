class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False]*n

        def DFS(adj, visited, u, nodes):
            visited[u] = True
            nodes.append(u)
            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, visited, v, nodes)
        
        cnt = 0
        for u in range(n):
            if not visited[u]:
                nodes = []
                DFS(adj, visited, u, nodes)
                all_connected = True
                for u in nodes:
                    if len(adj[u]) != len(nodes)-1:
                        all_connected = False
                        break
                if all_connected:
                    cnt += 1 
        
        return cnt