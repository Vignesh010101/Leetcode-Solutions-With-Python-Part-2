class Solution:
    
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        def rec(nums):
            if len(nums)==0:
                return 0
            nums.sort()
            psum=[nums[0]]
            for i in range(1,len(nums)):
                psum.append(psum[-1]+nums[i])
            s=psum[-1]
            ans=float("inf")
            temp=0
            n=len(nums)
            for i in range(n):
                ii=nums[i]
                temp+=ii
                s-=ii
                a=abs(ii*(i+1)-temp)+abs(ii*(n-i-1)-s)
                ans=min(ans,a)
                # print(ii,ans,a)
            return ans
        # if len(arr)%k==0:
        fans=0
        vis=set()
        for i in range(k):
                temparr=[]
                
                j=i
                while True:
                    if j%len(arr) not in vis:
                        vis.add(j%len(arr))
                        temparr.append(arr[j%len(arr)])
                    else:
                        break
                    j+=k
                # print(temparr)
                fans+=rec(temparr)
                
                    
            
        return fans
                
                    