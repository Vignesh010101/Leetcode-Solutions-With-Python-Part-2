class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n  = len(grid)+2, len(grid[0])
        grid =[[inf]*n]+grid+[[inf]*n]
       
        for j in range(1,n):
            found = False
            for i in range(1, m-1):

                if grid[i][j] <= min(grid[i-1][j-1],
                                     grid[i  ][j-1],
                                     grid[i+1][j-1]): grid[i][j] = inf
                
                else: found = True
       
            if not found: break
            
        else: return n-1

        return j-1