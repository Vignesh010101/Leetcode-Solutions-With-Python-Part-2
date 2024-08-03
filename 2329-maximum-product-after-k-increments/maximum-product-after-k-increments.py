class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007
        nums.sort()
        for i, x in enumerate(nums): 
            target = nums[i+1] if i+1 < len(nums) else inf
            diff = (target-x) * (i+1)
            if diff <= k: k -= diff 
            else: break 
        q, r = divmod(k, i+1)
        ans = pow(x+q+1, r, mod) * pow(x+q, i+1-r, mod) % mod
        for ii in range(i+1, len(nums)): 
            ans = ans * nums[ii] % mod
        return ans