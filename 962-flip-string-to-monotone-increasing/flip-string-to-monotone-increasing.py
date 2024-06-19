from itertools import accumulate
from functools import reduce

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return reduce(lambda acc, curr: acc if int(curr[0]) else min(curr[1], acc + 1), zip(s, accumulate(map(int, s))), 0)