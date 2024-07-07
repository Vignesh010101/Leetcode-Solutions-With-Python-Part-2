class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n,s,maxi=0,0,arr[0]
        for i in arr:
            s+=i
            n+=1
            if maxi<i:
                maxi=i
        if s==target:
            return maxi
        def arrsum(n):
            s=0
            for i in arr:
                if i<n:
                    s+=i
                else:
                    s+=n
            return s
        ans1,ans2=maxi,maxi
        i,j=target//n,maxi
        while i<=j:
            mid=(i+j)//2
            k=arrsum(mid)
            if k==target:
                return mid
            elif k>target:
                ans1=mid
                j=mid-1
            else:
                i=mid+1
        i,j=target//n,maxi
        while i<=j:
            mid=(i+j)//2
            k=arrsum(mid)
            if k==target:
                return mid
            elif k<target:
                ans2=mid
                i=mid+1
            else:
                j=mid-1
        m1,m2=abs(target-arrsum(ans1)),abs(target-arrsum(ans2))
        if m1==m2:
            return min(ans1,ans2)
        elif m1<m2:
            return ans1
        return ans2