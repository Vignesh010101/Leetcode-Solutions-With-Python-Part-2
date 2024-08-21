class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        r = 0
        for l in range(len(nums)):
            while r < len(nums) and nums[r] <= nums[l]+2*k:
                r += 1
            ans = max(ans, r-l)
            if r == len(nums):
                break
        return ans
            