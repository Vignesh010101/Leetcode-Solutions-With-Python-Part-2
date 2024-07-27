class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        maximum=0
        minimum=0
        for i in nums:
            maximum=max(maximum,i-minimum)
            minimum=min(minimum,i-maximum)
        return maximum