class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Find the maximum elements in each row and column
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]  # Efficient zip for columns

        # Calculate the total increase while maintaining the skyline
        total_increase = 0
        for r in range(n):
            for c in range(n):
                total_increase += min(row_max[r], col_max[c]) - grid[r][c]

        return total_increase