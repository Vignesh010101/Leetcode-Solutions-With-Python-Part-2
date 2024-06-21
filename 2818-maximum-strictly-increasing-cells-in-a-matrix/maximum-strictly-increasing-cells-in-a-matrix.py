class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mp = dict()
        for i in range(m):
            for j in range(n):
                if mat[i][j] not in mp:
                    mp[mat[i][j]] = []
                mp[mat[i][j]].append((i, j))
        row, col = [0] * m, [0] * n
        tmpR, tmpC = [0] * m, [0] * n
        for k, v in sorted(mp.items()):
            for (x, y) in v:
                s = max(row[x], col[y])
                tmpR[x] = max(tmpR[x], s + 1)
                tmpC[y] = max(tmpC[y], s + 1)
            for (x, y) in v:
                row[x] = tmpR[x]
                col[y] = tmpC[y]
        return max(row)