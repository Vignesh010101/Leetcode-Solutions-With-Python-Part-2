import heapq
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        q = [(0, grid[start[0]][start[1]], start[0], start[1])]
        visit = set()
        result = []
        while q:
            dis, price, x, y = heapq.heappop(q)
            if (x, y) in visit:
                continue
            visit.add((x, y))
            if price != 1 and price >= pricing[0] and price <= pricing[1]:
                result.append([x, y])
            if len(result) == k:
                return result
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) not in visit:
                    temp = grid[new_x][new_y]
                    if temp == 0:
                        continue
                    elif temp == 1:
                        heapq.heappush(q, (dis + 1, 1, new_x, new_y))
                    else:
                        heapq.heappush(q, (dis + 1, temp, new_x, new_y))
        
        return result