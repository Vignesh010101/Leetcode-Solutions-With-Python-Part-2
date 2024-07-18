class Solution:
    def dfs(self,node,grid,hasApple,visited):
        visited[node]=1
        ct=0
        for i in grid[node]:
            if visited[i]==1:
                continue
            x=self.dfs(i,grid,hasApple,visited)
            if x!=-1:
                ct+=x
                ct+=2
        if ct>0 or hasApple[node]==True:
            return ct
        return -1



    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        grid=[[] for i in range(n)]
        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)
        visited=[0]*n
        x=self.dfs(0,grid,hasApple,visited)
        if x==-1:
            return 0
        return x