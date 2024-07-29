class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        n = len(rides)
        dp = [0]*(n+1)
        start = [s for s,e,t in rides]

        for i in range(n-1,-1,-1):
            nextIndex = bisect_left(start,rides[i][1])
            dp[i] = max(dp[i+1], rides[i][1]-rides[i][0]+rides[i][2] + dp[nextIndex])

        return dp[0]