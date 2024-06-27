class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        lst=[[0]*4 for i in range(n)]
        visited=[0]*(n+1)
        adj=[[] for i in range(n+1)]
        for i,j in paths:
            adj[i].append(j)
            adj[j].append(i)
        visited[0]=1
        ans=[0]*n
        for i in range(1,n+1):
            st=[i]
            while st:
                x=st.pop(0)
                ans[x-1]=lst[x-1].index(0)+1
                for i in adj[x]:
                    if visited[i]==0:
                        st.append(i)
                        visited[i]=1
                    lst[i-1][ans[x-1]-1]=1
        return ans
            

        