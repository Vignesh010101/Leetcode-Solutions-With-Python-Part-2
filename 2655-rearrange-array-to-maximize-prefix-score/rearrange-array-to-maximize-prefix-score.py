class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return sum(vy>0 for vy in accumulate(sorted(nums, reverse=True)))