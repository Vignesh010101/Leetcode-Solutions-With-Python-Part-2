from fractions import Fraction
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        l=[]
        stockPrices.sort()
        c=None
        k=0
        for i,j in pairwise(stockPrices):
            x=Fraction(j[1]-i[1],j[0]-i[0])
            if x!=c:
                k+=1
                c=x
        return k