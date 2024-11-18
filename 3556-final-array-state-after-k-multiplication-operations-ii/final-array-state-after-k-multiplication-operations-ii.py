from heapq import *
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier==1: return nums
        mod=1_000_000_007
        if len(nums)==1:
            nums[0]=(nums[0]*pow(multiplier,k,mod))%mod
            return nums
        while True and k>0:
            mn=min(nums)
            mx=max(nums)
            if mn*multiplier>mx: break
            for i in range(len(nums)):
                if k>0 and nums[i]==mn:
                    k-=1
                    nums[i]*=multiplier
        nums=[[nums[i],i] for i in range(len(nums))]
        nums.sort()
        val1,val2=k//len(nums),k//len(nums)+1
        remaining=k%len(nums)
        for i in range(remaining):
            nums[i][0]=(nums[i][0]*pow(multiplier,val2,mod))%mod
        for i in range(remaining,len(nums)):
            nums[i][0]=(nums[i][0]*pow(multiplier,val1,mod))%mod
        nums.sort(key=lambda x:x[1])
        return [i[0] for i in nums]