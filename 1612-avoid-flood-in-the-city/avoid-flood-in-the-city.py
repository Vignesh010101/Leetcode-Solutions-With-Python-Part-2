def find_gt(a, x):
    'Find value higher than & closest to x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    return None 

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fullLakes = {}
        dryDays = []
        res = [-1]*len(rains)

        for day, lake in enumerate(rains):
            if lake == 0:
                dryDays.append(day)
                res[day] = 1  # by default select first lake to empty
            else:
                if lake in fullLakes:
                    # Empty it
                    dayOfFull = fullLakes[lake]
                    dryDay = find_gt(dryDays, dayOfFull)
                    if dryDay is None: return [] # cannot avoid Flood
                    dryDays.remove(dryDay)
                    res[dryDay] = lake

                fullLakes[lake] = day 

        return res 