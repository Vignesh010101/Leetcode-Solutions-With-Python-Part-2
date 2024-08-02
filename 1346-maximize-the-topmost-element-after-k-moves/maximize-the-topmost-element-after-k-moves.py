class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1 if k % 2 == 1 else nums[0]
        if k <= 1:
            return nums[k]
        if k < len(nums):
            return max(max(nums[:k-1]), nums[k])
        if k < len(nums) + 2: 
            return max(nums[:k-1])
        return max(nums)