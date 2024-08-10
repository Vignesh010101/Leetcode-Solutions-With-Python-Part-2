class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row1 = [sum(row) for row in grid]
        col1 = [sum(col) for col in zip(*grid)] 

        for i, row in enumerate(grid):
            for j in range(n):
                row[j]=2*(row1[i] + col1[j])-(m + n)
        return grid
        