class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans=0
        for n in nums:
            ans|=n
        return ans