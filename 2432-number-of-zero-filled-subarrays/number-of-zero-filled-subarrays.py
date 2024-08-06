class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans,zero_sum = 0,0
        for cur in nums+[1]:
            if cur: zero_sum=0
            else: zero_sum +=1
            ans += zero_sum
        return ans    