class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fSeries = [1,1]
        while fSeries[-1] <= k:
            fSeries.append(fSeries[-1]+fSeries[-2])
        ans = 0
        while k>0:
            if fSeries[-1]>k:
                fSeries.pop()
            else:
                ans+=1
                k = k-fSeries[-1]
        return ans
            


        