class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(row,col):
            grid[row][col]=0
            for d in directions:
                r = row+d[0]
                c = col+d[1]
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                    dfs(r,c)
        for i in range(len(grid)):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][len(grid[0])-1]==1:
                dfs(i,len(grid[0])-1)
        for i in range(len(grid[0])):
            if grid[0][i]==1:
                dfs(0,i)
            if grid[len(grid)-1][i]==1:
                dfs(len(grid)-1,i)
        count=0
        # print(visited)
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
        return count