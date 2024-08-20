class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if set(nums)=={0}:return 0
        frst_ind_one=nums.index(1)
        last_ind_one=nums[::-1].index(1)
        nums=nums[frst_ind_one:(len(nums)-last_ind_one)]
        res,zeros_count=1,0
        mod = 10**9+7
        for i in nums:
            if i==0:
                zeros_count+=1
            elif zeros_count>0:
                res=res*(zeros_count+1)
                res=res%mod
                zeros_count=0
        return res