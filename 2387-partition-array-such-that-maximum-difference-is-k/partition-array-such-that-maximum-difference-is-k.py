class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        subsequence = 1
        nums = sorted(nums)
        smallest = nums[0]
        if nums[-1] - smallest <= k:
            return subsequence

        for largest in nums:
            if largest - smallest > k:
                subsequence += 1
                smallest = largest
                
        return subsequence
        