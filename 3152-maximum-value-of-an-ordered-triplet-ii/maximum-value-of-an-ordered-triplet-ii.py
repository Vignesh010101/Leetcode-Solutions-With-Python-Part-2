class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = diff = prefix = 0 
        for i, x in enumerate(nums): 
            ans = max(ans, x*diff)
            diff = max(diff, prefix-x)
            prefix = max(prefix, x)
        return ans    