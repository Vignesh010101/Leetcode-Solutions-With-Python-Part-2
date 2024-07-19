class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minirow={min(v) for v in matrix}
        maxicol={max(c) for c in zip(*matrix)}
        return list(minirow & maxicol)