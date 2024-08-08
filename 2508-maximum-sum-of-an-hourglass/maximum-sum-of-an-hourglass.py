class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return -1

        res = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                temp = grid[i][j]
                temp += grid[i - 1][j] + grid[i - 1][j - 1] + grid[i - 1][j + 1]
                temp += grid[i + 1][j] + grid[i + 1][j - 1] + grid[i + 1][j + 1]

                if temp > res:
                    res = temp

        return res