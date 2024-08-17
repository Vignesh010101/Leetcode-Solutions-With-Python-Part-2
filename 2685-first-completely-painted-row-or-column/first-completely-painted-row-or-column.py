class Solution:
    def firstCompleteIndex(self, arr: List[int], matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        row, col = [0 for i in range(m)], [0 for i in range(n)]
        d = {}
        for i in range(m):
            for j in range(n):
                d[matrix[i][j]] = (i,j)
        for i in range(m * n):
            y, x = d[arr[i]]
            row[y] += 1
            col[x] += 1
            if row[y] >= n or col[x] >= m:
                return i
        return -1


