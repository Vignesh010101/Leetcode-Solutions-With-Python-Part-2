class Solution:
    def maxPower(self, nums: List[int], r: int, k: int) -> int:
        def check(m):
            res=0
            temp = nums.copy()
            curr = sum(temp[:r])
            for i in range(n):
                if i+r < n:
                    curr+=temp[i+r]
                if i-r-1 > -1:
                    curr-=temp[i-r-1]
                if curr<m:
                    diff = m-curr
                    rr = min(i+r,n-1)
                    curr+=diff     #wasted 1 hour because i forgot this
                    temp[rr]+=diff
                    res+=diff
            return res<=k
        
        n = len(nums)
        s,e = 0,sum(nums)+k
        while s<e:
            m = s+e+1>>1
            if check(m):
                s=m
            else:
                e=m-1
        return s
                    