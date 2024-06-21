MX = 100001
lpf = [0] * MX
for i in range(2, MX):
    if lpf[i] == 0:
        for j in range(i, MX, i):
            lpf[j] = i

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.ans = 0
        def dfs(node, par):
            prime = lpf[node] == node

            s0 = s1 = 0
            for nei in adj[node]:
                if nei != par:
                    c0, c1 = dfs(nei, node)
                    
                    # answer for LCA(u, v) = node, node not in [u, v]
                    if prime:
                        self.ans += s0 * c0
                    else:
                        self.ans += s0 * c1 + s1 * c0
                    
                    s0 += c0
                    s1 += c1
            
            # answer for LCA(u, v) = node, node in [u, v]
            if not prime:
                self.ans += s1
                return s0 + 1, s1
            else:
                self.ans += s0
                return 0, s0 + 1

        dfs(1, 0)
        return self.ans