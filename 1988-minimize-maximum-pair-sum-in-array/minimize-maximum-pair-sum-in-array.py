class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(map(add, islice(nums,0,len(nums)//2), reversed(nums)))