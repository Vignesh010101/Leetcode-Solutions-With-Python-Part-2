class Solution:
    def dfs(self,node,visited,ans,value,lst):
        # print(node)
        visited[node]=1
        for i in lst[node]:
            if visited[i]==0:
                self.dfs(i,visited,ans,value,lst)
            x=value[i]
            # print(node,i,value[node],x)
            if x<value[node]:
                value[node]=x
                ans[node]=ans[i]
        return 

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        visited=[0]*n
        lst=[[] for i in range(n)]
        for i,j in richer:
            lst[j].append(i)
        # print(lst)
        ans=[i for i in range(n)]
        value=[quiet[i] for i in range(n)]
        for i in range(n):
            if visited[i]==0:
                self.dfs(i,visited,ans,value,lst)
        return ans 