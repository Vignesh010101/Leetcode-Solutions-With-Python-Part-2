class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        max_above = [[0] * n for _ in range(m)]
        max_below = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                above = max_above[r - 1][c] if r else -math.inf
                max_above[r][c] = max(board[r][c], above)

        for r in range(m - 1, -1, -1):
            for c in range(n):
                below = max_below[r + 1][c] if r + 1 < m else -math.inf
                max_below[r][c] = max(board[r][c], below)

        def top3Cols(row):
            return heapq.nlargest(3, ((x, i) for i, x in enumerate(row)))

        def bestOfRows(row1, row2, row3):
            cols1, cols2, cols3 = map(top3Cols, (row1, row2, row3))
            ans = -math.inf
            for x1, c1 in cols1:
                for x2, c2 in cols2:
                    for x3, c3 in cols3:
                        if len({c1, c2, c3}) == 3:
                            ans = max(ans, x1 + x2 + x3)
            return ans

        ans = -math.inf
        for r in range(1, m - 1):
            ans = max(ans, bestOfRows(board[r], max_above[r - 1], max_below[r + 1]))

        return ans