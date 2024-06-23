class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        
        inf = 10**9+7
        dist = [[inf]*n for _ in range(n)]
        
        for u,v,w in roads: 
            dist[u][v] = min(dist[u][v],w)
            dist[v][u] = min(dist[v][u],w)
        
        def check(D,rem):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if D[i][k] < inf and D[k][j] <inf: 
                            D[i][j] = min(D[i][j],D[i][k]+D[k][j])
                            
            for x in rem:
                for y in rem:
                    if x == y:continue
                    if D[x][y]>maxDistance: return False
                    
            return True
                        
        ans = 0 
        for mask in range(1<<n):
            newDist = [dist[i].copy() for i in range(n)]
            
            rem = []
            for i in range(n):
                if (mask>>i)&1 == 0: 
                    for j in range(n):
                        newDist[i][j] = inf
                        newDist[j][i] = inf
                else: 
                    rem.append(i)
            
            if check(newDist,rem): 
                ans+=1
            
        
        return ans
            