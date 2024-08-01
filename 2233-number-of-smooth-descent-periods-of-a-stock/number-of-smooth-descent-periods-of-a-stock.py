class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp=[]
        for i in range(1,len(prices)):
            if(prices[i]-prices[i-1]==-1):
                dp.append(1)
            else:
                dp.append(0)
        c=[]
        res=0
        count=0
        for i in range(len(dp)):
            if(dp[i]==1):
                count+=1
            else:
                c.append(count)
                count=0
        c.append(count)
        for i in c:
            if(i==1):
                res+=1
            else:
                res+=(i*(i+1))//2
        res+=len(prices)
        return(res)
            