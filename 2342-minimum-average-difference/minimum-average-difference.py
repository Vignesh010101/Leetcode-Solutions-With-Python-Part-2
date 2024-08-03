class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        pre,post=[nums[0]]*n,[nums[n-1]]*n
        for i in range(1,n):
            pre[i]=(nums[i]+pre[i-1])
        for i in range(n-2,-1,-1):
            post[i]=(nums[i]+post[i+1])
        m,f=1000000,n-1
        for i in range(n):
            x=pre[i]//(i+1)
            if i==n-1:
                y=0
            else:
                y=post[i+1]//(n-i-1)
            if m>abs(x-y):
                m=abs(x-y)
                f=i
        return f