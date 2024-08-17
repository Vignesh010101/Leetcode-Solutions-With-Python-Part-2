class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            # terminating criteria 
            if 0 > i or i >= m or 0 > j or j >= n or grid[i][j] == 0:
                return 0
            
            val = grid[i][j]
            grid[i][j] = 0 # set to 0, no need to revisit
            return val + bfs(i - 1, j) + bfs(i + 1, j) + bfs(i, j - 1) + bfs(i, j + 1)

        m, n = len(grid), len(grid[0])
        output = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    val = bfs(i, j)
                    if output < val:
                        output = val
        
        return output

                