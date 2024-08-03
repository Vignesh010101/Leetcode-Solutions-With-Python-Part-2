class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        choose = 1
        total = 0
        for r in range(n):
            total += nums[r] * choose
            choose = choose * ((n-1)-r) // (r+1)
        return total % 10