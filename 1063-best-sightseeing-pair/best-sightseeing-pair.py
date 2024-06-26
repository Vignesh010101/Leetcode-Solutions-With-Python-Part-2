class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = ans = 0
        for n in values:
            if n+best > ans:
                ans = n+best
            if n > best:
                best = n-1
            else:
                best -= 1
        return ans