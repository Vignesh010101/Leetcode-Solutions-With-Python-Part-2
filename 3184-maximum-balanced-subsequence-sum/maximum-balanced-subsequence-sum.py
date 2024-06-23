class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        if max(nums) < 1:
            return max(nums)
        nums_idx = []
        for idx,num in enumerate(nums):
            if num > 0:
                nums_idx.append((num-idx,num))
        dp = SortedList([nums_idx[0]])
        for num_idx,num in nums_idx[1:]:
            idx = dp.bisect_right((num_idx,inf))
            res = num + (dp[idx-1][1] if idx > 0 else 0)
            while idx < len(dp) and res > dp[idx][1]:
                dp.remove(dp[idx])
            dp.add((num_idx,res))
        return max((i for _,i in dp))