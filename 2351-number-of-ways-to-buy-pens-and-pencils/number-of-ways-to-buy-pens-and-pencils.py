class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if total < cost1 and total < cost2:
            return 1
        ways = 0
        if cost1 > cost2:
            for i in range(0, (total // cost1)+1):
                rem = total - (i * cost1)
                ways += (rem // cost2) + 1
            return ways
        for i in range(0, (total // cost2)+1):
            rem = total - (i * cost2)
            ways += (rem // cost1) + 1
        return ways