class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            if dp[i] == -1: continue
            for j in range(i + 1, len(nums)):
                if abs(nums[j] - nums[i]) <= target:   
                    dp[j] = max(dp[i] + 1, dp[j])
        return dp[-1]