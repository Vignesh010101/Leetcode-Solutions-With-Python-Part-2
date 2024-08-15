class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        diff = [
                [2, 1],
                [1, 2],
            ]
        new = defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                new[grid[i][j]].append(i)
                new[grid[i][j]].append(j)     
        if new[0] != [0,0]:
            return False
        for i in range((n*n)-1):
            row = abs(new[i][0] - new[i+1][0])
            col = abs(new[i][1] - new[i+1][1])
            #print(row,col)
            if [row,col] not in diff:
                return False
        return True
        
        