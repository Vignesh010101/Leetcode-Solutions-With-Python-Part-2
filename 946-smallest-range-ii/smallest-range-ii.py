class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        minima, maxima = min( nums ), max( nums )
        if maxima - minima >= 4 * k:
            return maxima - minima - 2 * k
        if maxima - minima <= k:
            return maxima - minima
        interval = sorted( [i for i in nums if maxima - 2 * k < i < minima + 2 * k] 
                            + [maxima - 2 * k, minima + 2 * k] )
        return min( a + 2 * k - b for a, b in zip( interval, interval[1:] ) )