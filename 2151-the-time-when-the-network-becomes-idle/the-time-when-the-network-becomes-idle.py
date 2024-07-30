class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distance = [None] * len(patience)
        distance[0] = 0
        queue = deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] is None:
                    distance[neighbor] = 1 + distance[node]
                    queue.append(neighbor)

        def getLastSend(n: int) -> int:
            if patience[n] >= 2 * distance[n]:
                return 0
            if (2 * distance[n]) % patience[n] == 0:
                return 2 * distance[n] - patience[n]
            return 2 * distance[n] - (2 * distance[n] % patience[n])

        maxTime = max(getLastSend(n) + 2 * distance[n] for n in range(1, len(patience)))

        return maxTime + 1