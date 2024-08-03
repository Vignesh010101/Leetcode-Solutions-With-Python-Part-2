class Solution(object):
    def waysToSplitArray(self, nums):
        lSum, rSum = 0, sum(nums)
        ans = 0
        for i in range(len(nums) - 1):
            lSum += nums[i]
            rSum -= nums[i]
            if lSum >= rSum: ans += 1
        return ans