import numpy as np

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = np.array(grid, dtype=int).reshape(-1)

        if 0 != np.ptp(np.mod(grid, x)):
            return -1
        return int(np.abs(grid - np.median(grid)).sum() / x)