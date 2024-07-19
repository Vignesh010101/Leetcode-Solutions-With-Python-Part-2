class Solution:
    def dfs(self,node,grid,visited,fst,labels):
        visited[node]=1
        lst=[0]*26
        lst[ord(labels[node])-97]=1
        for i in grid[node]:
            if visited[i]==1:
                continue
            x=self.dfs(i,grid,visited,fst,labels)
            for j in range(26):
                lst[j]+=x[j]
        fst[node]=lst[ord(labels[node])-97]
        return lst

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        grid=[[] for _ in range(n)]
        for i,j in edges:
            grid[i].append(j)
            grid[j].append(i)

        visited=[0]*n
        fst=[0]*n
        self.dfs(0,grid,visited,fst,labels)
        return fst