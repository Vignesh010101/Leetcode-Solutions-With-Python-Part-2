class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        found=False
        from functools import cache

        @cache
        def solve(i):
            nonlocal n,nums,found
            if i<0:
                return True
            if not found:
                res=False
                if i-1>=0 and nums[i]==nums[i-1]:
                    res=res or solve(i-2)
                if i-2>=0 and (nums[i-2]==nums[i-1]==nums[i] or nums[i-2]+2==nums[i-1]+1==nums[i]):
                    res=res or solve(i-3)
                found=found or res
                return res
        
        return solve(n-1)