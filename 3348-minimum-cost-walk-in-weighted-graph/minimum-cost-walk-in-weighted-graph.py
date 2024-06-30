class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Define the find function to find the parent node of a given node
        def find(node: int) -> int:
            # If the node is its own parent, return the node
            if node == par[node]: return node
            # Apply path compression and return the parent node
            par[node] = find(par[node])
            return par[node]
        
        # Define the union function to merge two nodes and update their weights
        def union(u: int, v: int, w: int) -> int:
            # Find the parents of the two nodes
            x, y = find(u), find(v)
            # Update the weight of the parent node
            wgt[y] &= wgt[x] & w
            # Set the parent of the first node to be the second node
            par[x] = y
        
        # Define the findwgt function to find the weight of a query
        def findwgt(query: list) -> int:
            s, t = query
            # If the source and target nodes are the same, return 0
            if s == t: return 0
            # If the source and target nodes have different parents, return -1
            if find(s) != find(t): return -1
            # Return the weight of the parent node
            return wgt[find(s)]
        
        # Initialize parent, answer, and weight lists
        par, ans, wgt = list(range(n)), [], [(1<<31)-1] * n
        
        # Apply union operation on each edge
        for edge in edges:
            union(*edge)
        
        # Return the weights for each query using the findwgt function
        return map(findwgt, queries)