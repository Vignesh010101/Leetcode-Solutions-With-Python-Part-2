class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        sm = lambda n: sum(map(int,list(str(n))))
        zeros, diff = 10, 0
        while sm(n + diff) > target: 
            diff = zeros - n%zeros
            zeros*= 10                          
        return diff                             