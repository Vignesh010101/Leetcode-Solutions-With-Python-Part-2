class Solution:
    def buildMatrix(self, k: int, row: List[List[int]], col: List[List[int]]) -> List[List[int]]:
        adj_l_A = [[] for i in range(k+1)]
        indegree_A = [0]*(k+1)
        for u,v in row:
            adj_l_A[u].append(v)
            indegree_A[v]+=1
        queue1 = []
        for i in range(1,k+1):
            if indegree_A[i]==0:
                queue1.append(i)
        adj_l_B = [[] for i in range(k+1)]
        indegree_B = [0]*(k+1)
        for u ,v in col:
            adj_l_B[u].append(v)
            indegree_B[v]+=1
        queue2 = []
        for i in range(1,k+1):
            if indegree_B[i]==0:
                queue2.append(i)


        
        def topo_sort(queue,res,adj_list,indegree):
            while queue:
                curr = queue.pop(0)
                res.append(curr)
                for i in adj_list[curr]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
            return res
        Row = topo_sort(queue1,[],adj_l_A,indegree_A)
        Col = topo_sort(queue2,[],adj_l_B,indegree_B)
        if len(Row)==k and len(Col)==k:
            grid = [[0 for i in range(k)] for j in range(k)]
            ind = {}
            for i in range(k):
                ind[Col[i]] = i
            for i in range(k):
                j = ind[Row[i]]
                grid[i][j] = Row[i]
            return grid
        return []


        