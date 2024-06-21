from heapq import heapify, heappush, heappop
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        n = len(usageLimits)


        def poss(groups):
            sub = [usageLimits[0]]
            for i in range(1, n):
                sub.append(usageLimits[i] - usageLimits[i-1])
            for i in range(-groups, 0, 1):
                sub[i] -= 1
            for i in accumulate(list(accumulate(sub))):
                if i < 0:
                    return False
            return True
        

        l, r = 0, len(usageLimits)
        
        while l < r:
            mid = (l + r + 1) // 2
            if poss(mid):
                l = mid
            else:
                r = mid - 1
        return l