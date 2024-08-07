class Solution:          
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        dist = endPos-startPos

        if k%2 != dist%2 or abs(dist) > k: return 0

        return comb(k, (dist+k)//2) %1_000_000_007