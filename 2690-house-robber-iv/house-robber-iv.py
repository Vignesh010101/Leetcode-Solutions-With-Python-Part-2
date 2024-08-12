class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible(v, r):
            i = 0
            while i < len(nums) and r > 0:
                if nums[i] <= v:
                    r -= 1
                    i += 2
                else:
                    i += 1
            return r==0
        items = list(sorted(set(nums)))
        lo, hi = 0, len(items) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if possible(items[m], k):
                hi = m
            else:
                lo = m + 1
        return items[lo]
