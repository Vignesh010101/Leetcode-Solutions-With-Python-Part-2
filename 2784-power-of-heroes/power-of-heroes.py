class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        result,t=0,0
        mod=10**9+7
        for num in sorted(nums):
            result=(result+(t+num)*num*num)%mod
            t=(2*t+num)%mod
        return result