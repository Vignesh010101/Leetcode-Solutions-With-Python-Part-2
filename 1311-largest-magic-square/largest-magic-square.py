class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        rowPrefixSum = [[0] * (n + 1) for r in range(m)]
        for r in range(m):
            for c in range(n):
                rowPrefixSum[r][c + 1] = rowPrefixSum[r][c] + grid[r][c]
                        
        columnPrefixSum = [[0] * (m + 1) for c in range(n)]
        for c in range(n):
            for r in range(m):
                columnPrefixSum[c][r + 1] = columnPrefixSum[c][r] + grid[r][c]

        k = min(m, n)
        while 1 < k:
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    z = rowPrefixSum[r][c + k] - rowPrefixSum[r][c]
                    ok = 1
                    for i in range(k):
                        if z != rowPrefixSum[r + i][c + k] - rowPrefixSum[r + i][c] or z != columnPrefixSum[c + i][r + k] - columnPrefixSum[c + i][r]:
                            ok = 0
                            break
                    if ok:
                        diagZ1 = 0
                        diagZ2 = 0
                        for i in range(k):
                            diagZ1 += grid[r + i][c + i]
                            diagZ2 += grid[r + i][c + k - i - 1]
                        if z == diagZ1 == diagZ2:
                            return k
            k -= 1
        return 1
