from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        
        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return
            
            grid2[i][j] = 0
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i - 1, j)
        
        # Removing all the non-common sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        count = 0
        # Counting sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    count += 1
        
        return count
