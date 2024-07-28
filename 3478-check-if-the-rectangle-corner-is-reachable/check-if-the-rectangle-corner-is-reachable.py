class Solution:
    def canReachCorner(self, X: int, Y: int, A: List[List[int]]) -> bool:
        def find(i):
            if f[i] != i:
                f[i] = find(f[i])
            return f[i]

        n = len(A)
        f = list(range(n + 2))
        for i in range(n):
            x, y, r = A[i]
            if x - r <= 0 or y + r >= Y:
                f[find(n)] = find(i)
            if x + r >= X or y - r <= 0:
                f[find(n + 1)] = find(i)
            for j in range(i):
                x2, y2, r2 = A[j]
                if (x - x2) ** 2 + (y - y2) ** 2 <= (r + r2) ** 2:
                    f[find(i)] = find(j)
        return find(n) != find(n + 1)