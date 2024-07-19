class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=defaultdict(list)

        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))

        def dfs(nodes, parent):
            count=0
            for neighbor, direction in graph[nodes]:
                if neighbor!=parent:
                    count+=direction
                    count+=dfs(neighbor, nodes)
            return count

        return dfs(0,-1)