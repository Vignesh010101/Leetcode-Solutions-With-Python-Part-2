class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        mask = 0
        for x in nums: 
            if x & x-1 == 0: mask |= x 
        for i in range(32): 
            if not mask & 1<<i: return 1 << i 