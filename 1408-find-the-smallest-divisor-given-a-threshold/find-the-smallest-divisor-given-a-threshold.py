from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)

        while l <= r:
            mid = (l + r) // 2
            if sum(ceil(j / mid) for j in nums) <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        return l