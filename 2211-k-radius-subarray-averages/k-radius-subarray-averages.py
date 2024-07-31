class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        r = 2*k + 1
        if r > n:
            return ans
        s = 0
        for i in range(r):
            s+=nums[i]
        span = k+k+1-n  # -n so wo dont have to deal with last iteration 
        for i in range(n-k-k):
            ans[i+k] = s // r
            s += nums[i+span] - nums[i]
        return ans