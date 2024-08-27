class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)] 
        for i, (a, b) in enumerate(edges):
            adj[a].append((b, succProb[i]))  
            adj[b].append((a, succProb[i]))  
        probabilities = [0] * n  
        probabilities[start] = 1  
        pq = []  
        heapq.heappush(pq, (-1, start))  
        while pq:
            probability, node = heapq.heappop(pq)  
            probability *= -1  

            if node == end:  
                return probability

            if probability < probabilities[node]:  
                continue

            for neighbor, edge_prob in adj[node]:  
                new_prob = probability * edge_prob  
                if new_prob > probabilities[neighbor]:  
                    probabilities[neighbor] = new_prob  
                    heapq.heappush(pq, (-new_prob, neighbor))  

        return 0
        