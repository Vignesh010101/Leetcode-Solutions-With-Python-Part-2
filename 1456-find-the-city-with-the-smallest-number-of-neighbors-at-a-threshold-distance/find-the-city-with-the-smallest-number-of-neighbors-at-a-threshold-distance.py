class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        k = float("inf")
        cost = [[k for _ in range(n)] for _ in range(n)]
        
        for u, v, w in edges:
            cost[u][v] = cost[v][u] = w

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    cost[j][k] = min(cost[j][i] + cost[i][k], cost[j][k])

        ans = -1
        k = float("inf")

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and cost[i][j] <= distanceThreshold:
                    count += 1

            if k >= count:
                ans = i
                k = count

        return ans