class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        odds = [a for a in graph if len(graph[a]) % 2 == 1]
        if not odds:
            return True
        elif len(odds) > 4 or len(odds) == 1 or len(odds) == 3:
            return False
        elif len(odds) == 2:
            a, b = odds[0], odds[1]
            if a not in graph[b]:
                return True
            for i in range(1, n + 1):
                if i not in graph[a] and i not in graph[b]:
                    return True
            return False
        else:
            a, b, c, d = odds[0], odds[1], odds[2], odds[3]
            if a not in graph[b] and c not in graph[d]:
                return True
            if a not in graph[c] and b not in graph[d]:
                return True
            if a not in graph[d] and b not in graph[c]:
                return True
            return False