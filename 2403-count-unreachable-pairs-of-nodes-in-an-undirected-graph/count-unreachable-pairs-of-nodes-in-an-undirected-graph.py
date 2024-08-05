class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [ [] for _ in range(0,n) ]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        res = 0
        visited = [0 for _ in range(0,n)]
        dq = deque()
        for i in range(0,n):
            if(visited[i]==0):
                dq.append(i);
                visited[i] = 1
                curCount = 1
                while(len(dq)>0):
                    v = dq.popleft()
                    for neib in graph[v]:
                        if(visited[neib]== 0 ):
                            curCount += 1
                            visited[neib]=1
                            dq.append(neib)
                res+= curCount*(n-curCount)
        return res//2
               