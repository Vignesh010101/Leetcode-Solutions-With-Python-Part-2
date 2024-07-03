class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if max(max(grid)) == 0 or min(min(grid)) == 1: return -1
        ROWS, COLS = len(grid), len(grid[0])
        queue, visit = deque(), set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r,c,0))
                    visit.add((r,c))
        res = 0
        while queue:
            r,c,dist = queue.popleft()
            for i, j in dirs:
                next_row = r + i
                next_col = c + j
                if 0 <= next_row < ROWS and 0 <= next_col < COLS and (next_row, next_col) not in visit:
                    new_dist = dist + 1
                    res = max(res, new_dist)
                    queue.append((next_row,next_col,new_dist))
                    visit.add((next_row,next_col))
        return res
        
            