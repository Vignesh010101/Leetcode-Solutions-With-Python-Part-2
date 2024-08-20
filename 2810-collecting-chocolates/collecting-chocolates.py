from sortedcontainers import SortedList

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        @cache
        def cost(shift):
            sl = SortedList(nums[:shift + 1])
            ans = 0
            for i in range(n):
                ans += sl[0]
                sl.discard(nums[i])
                sl.add(nums[(i + shift + 1) % n])
            ans = ans + x * shift
            return ans
        
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if cost(m) > cost(m-1):
                r = m
            else:
                l = m + 1
        return cost(l-1)     