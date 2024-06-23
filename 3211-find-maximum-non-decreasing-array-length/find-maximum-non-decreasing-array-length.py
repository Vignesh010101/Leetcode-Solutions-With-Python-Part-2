class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        nums+=[float('inf')]
        presum=[0]+list(accumulate(nums))

        n, dp, prev, cur = len(nums)-1, Counter(), Counter(), 0

        for i in range(n):
            i+=1
            cur=max(cur,prev[i])
            dp[i]=(i-cur-1) + dp[cur]
            idx=bisect.bisect_left(presum,2*presum[i]-presum[cur])   
            prev[idx]=i
        return n-dp[n]