class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        ans = [-1] * m

        def isValid(col):
            return 0 <= col < m

        for i in range(m):
            row = 0
            col = i

            while True:
                if row == n:
                    ans[i] = col
                    break

                if grid[row][col] == 1:
                    # pattern 1 => 1
                    if isValid(col + 1) and grid[row][col + 1] == 1:
                        col += 1
                    else:
                        break 
                else:
                    # pattern -1 <= -1
                    if isValid(col - 1) and grid[row][col - 1] == -1:
                        col -= 1
                    else:
                        break
                
                # a ball continue to fall
                row += 1

        return ans