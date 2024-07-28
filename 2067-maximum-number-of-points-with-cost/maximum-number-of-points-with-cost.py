class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Instead checking all possibilities, adjust upper row with max possible in each cell
        m, n = len(points), len(points[0])
        for i in range(1, m):
            # Spread upper row with max possible
            # Spread from left to right
            for j in range(1, n):
                points[i-1][j] = max(points[i-1][j], points[i-1][j-1]-1)
            # Spread from right to left
            for j in range(n-2, -1, -1):
                points[i-1][j] = max(points[i-1][j], points[i-1][j+1]-1)
            # Sum with upper row
            for j in range(n):
                points[i][j] += points[i-1][j]
        return max(points[m-1])