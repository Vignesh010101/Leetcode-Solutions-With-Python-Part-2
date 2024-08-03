class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return bisect_left(range(1, sum(candies) // k + 1), True, key=lambda c: sum(x // c for x in candies) < k)