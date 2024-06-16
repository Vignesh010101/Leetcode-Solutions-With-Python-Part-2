class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss=1
        result=0
        v=0

        while miss<=n:
            if v<len(nums) and nums[v]<=miss:
                miss+=nums[v]
                v+=1
            else:
                miss+=miss
                result+=1

        return result