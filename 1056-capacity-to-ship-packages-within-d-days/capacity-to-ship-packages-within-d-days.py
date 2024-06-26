import functools
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights)
        l, r = max(weights), sum(weights)
        m = None
        @functools.cache
        def _days(capacity:int) -> int:
            i = 0
            d = 0
            while i < N:
                d+=1
                tank = capacity
                while i < N and tank >= weights[i]:
                    tank-=weights[i]
                    i+=1
            return d
        while True:
            m = (l+r)//2
            if _days(m)==days and _days(m-1)<days:
                return m
            elif _days(m) <= days:
                r = m
            elif _days(m) > days:
                l = m
            if r-l<=1:
                if _days(l)<=days:
                    return l
                return r
            