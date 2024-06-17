class Solution:
    def maxPoints(self, grid, qs: List[int]) -> List[int]:
        queries = sorted(set(qs))
        res = {}
        rows, cols = len(grid), len(grid[0])
        q = [(grid[0][0], 0, 0)] # heap
        prevCount = 0

        for num in queries:
            count = prevCount

            while q:
                val, r, c = q[0]

                if val >= num: break # pop only when the condition satisfy else break
                else:
                    heappop(q)
                    grid[r][c] = None
                    count += 1

                    for i, j in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                        if 0 <= i < rows and 0 <= j < cols and grid[i][j] is not None:
                            heappush(q, (grid[i][j], i, j))
                            grid[i][j] = None

            res[num] = prevCount = count

        ans = [res[num] for num in qs]
        return ans