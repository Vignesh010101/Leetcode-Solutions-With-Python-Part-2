class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        R, C = 0, 1
        nr, nc = len(grid), len(grid[0])

        def get_nx(r, c):
            for r_nx, c_nx in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0 <= r_nx <= nr-1 and 0 <= c_nx <= nc-1:
                    yield r_nx, c_nx

        # main
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        start, end = (0, 0), (nr-1, nc-1)
        t_to_cells = defaultdict(set)
        t = 0
        t_to_cells[t].add(start)
        visited = {start}
        while True:
            for r, c in t_to_cells[t]:
                for r_nx, c_nx in get_nx(r, c):
                    if (r_nx, c_nx) in visited:
                        continue
                    if grid[r_nx][c_nx] > t+1:
                        t_diff = grid[r_nx][c_nx] - t
                        t_nx = t + t_diff if t_diff % 2 == 1 else t + t_diff + 1
                    else:
                        t_nx = t+1
                    if (r_nx, c_nx) == end:
                        return t_nx
                    t_to_cells[t_nx].add((r_nx, c_nx))
                    visited.add((r_nx, c_nx))
            t += 1