class Solution:
    def numRescueBoats(self, p: List[int], li: int) -> int:
        p.sort()
        n = len(p)
        lo, hi = 0, n-1 
        res, cur= 0, 0
        while lo<= hi: 
            res+=1
            if p[lo]+p[hi]<=li: 
                lo+=1
            hi-=1

        return res