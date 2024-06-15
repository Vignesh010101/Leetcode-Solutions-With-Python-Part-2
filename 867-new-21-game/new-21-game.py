class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0:
            return 1.0

        windowsum=0
        for i in range(k,k + maxPts):
            windowsum+= 1 if i<=n else 0

        dp={}
        for i in range(k-1,-1,-1):
            dp[i]=windowsum/maxPts
            remove=0
            if i+maxPts<=n:
                remove=dp.get(i+maxPts,1)
            windowsum+= dp[i]-remove
        return dp[0] 