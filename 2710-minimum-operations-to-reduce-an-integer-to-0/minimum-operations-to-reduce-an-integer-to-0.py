from math import log2

class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n:
            exp = round(log2(n))
            n = abs(2**exp - n)
            count += 1

        return count