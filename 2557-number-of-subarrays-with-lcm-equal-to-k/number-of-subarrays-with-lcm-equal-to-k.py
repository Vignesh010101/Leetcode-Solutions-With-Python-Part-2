from math import lcm

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            l = nums[i]
            for j in range(i, n):
                l = lcm(l, nums[j])
                if l == k:
                    result += 1
                elif l > k:
                    break
        return result