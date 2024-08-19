
from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:        
        m = len(grid)    # Rows
        n = len(grid[0]) # Columns
        
        topLeft = [[[] for _ in range(n)] for _ in range(m)]
        bottomRight = [[[] for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r > 0 and c > 0:
                    topLeft[r][c].extend( topLeft[r-1][c-1] + [grid[r-1][c-1]])
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r < m-1 and c < n-1:
                    bottomRight[r][c].extend( bottomRight[r+1][c+1] + [grid[r+1][c+1]])
        
        answer = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                answer[r][c] = abs(len(set(topLeft[r][c])) - len(set(bottomRight[r][c])))
        
        return answer