class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = [x for row in grid for x in row]
        if len(set(val%x for val in vals)) > 1: return -1 
        median = sorted(vals)[len(vals)//2] 
        return sum(abs(val - median)//x for val in vals)