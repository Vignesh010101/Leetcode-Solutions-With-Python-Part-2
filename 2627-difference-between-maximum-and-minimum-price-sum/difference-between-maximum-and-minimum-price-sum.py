class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        # 1 <= price[i] <= 10^^5
        # min value is value of the root itself
        # find max value from the root to any leaf
        
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        rtl = [[] for _ in range(n)]
        # first traversal to find the node to leaf path from each of the node (assume 0 is the root)
        def traverse1(node, parent):
            for nei in graph[node]:
                if nei == parent: continue
                traverse1(nei, node)
                
                child = rtl[nei][-1] # the max entry
                rtl[node].append(child + price[node])
                
            if not rtl[node]:
                rtl[node].append(price[node])
            
            rtl[node].sort()
            rtl[node] = rtl[node][-2:]  # keep at most 2 entry, we dont need more
            
        traverse1(0, -1)
        
        ans = 0
        # second traversal to compute the result from the parent, max parent path that not going through the current node
        def traverse2(node, parent):
            if parent != -1:
                if len(rtl[parent]) == 1: # only 1 path
                    rtl[node].append(price[parent] + price[node])
                else:
                    if rtl[node][-1] + price[parent] == rtl[parent][-1]: # this is the longest path, we take the next longest
                        rtl[node].append(rtl[parent][-2] + price[node])
                    else:
                        rtl[node].append(rtl[parent][-1] + price[node])
            
            rtl[node].sort()
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                traverse2(nei, node)
            
        traverse2(0, -1)
        return max(rtl[i][-1] - price[i] for i in range(n))
                
        
        
        
        