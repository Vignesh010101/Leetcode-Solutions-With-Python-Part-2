class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n+1)]

        for p1, p2 in dislikes:
            adj[p1].append(p2)
            adj[p2].append(p1)
        
        colors = [-1] * (n+1)

        def bfs(color_idx):
            q = collections.deque([color_idx])
            colors[color_idx] = 0

            while q:
                person = q.popleft()
                for neighbor in adj[person]:
                    if colors[neighbor] == colors[person]:
                        return False
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[person]
                        q.append(neighbor)
            
            return True

        for idx in range(1, len(colors)):
            if colors[idx] == -1:
                if not bfs(idx):
                    return False
        
        return True