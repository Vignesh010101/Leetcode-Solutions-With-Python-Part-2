class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = 0
        gaps = 0
        for rung in rungs:
            if rung-prev > dist:
                gaps += (rung-prev-1)//dist
            prev = rung
        return gaps