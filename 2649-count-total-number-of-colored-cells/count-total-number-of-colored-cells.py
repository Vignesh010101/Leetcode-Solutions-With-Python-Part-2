class Solution:
    def coloredCells(self, n: int) -> int:
        if n ==1 :
            return 1
        prev = 1
        for i in range(2,n):
            prev = prev + (i)*4
        return prev+4