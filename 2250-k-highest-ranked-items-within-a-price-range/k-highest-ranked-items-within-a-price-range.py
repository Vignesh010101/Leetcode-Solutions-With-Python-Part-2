class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        sx, sy = start
        pl, ph = pricing
        q = [(0, grid[sx][sy], sx, sy)]
        visited = set()
        res = []

        while q:
            dis, price, x, y = heapq.heappop(q)
            if (x, y) in visited: continue
            
            visited.add((x, y))
            
            if price != 1 and pl <= price <= ph: res.append([x, y])
            if len(res) == k: return res

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    val = grid[new_x][new_y]
                    if val == 0: continue
                    else: heapq.heappush(q, (dis + 1, val, new_x, new_y))
        return res