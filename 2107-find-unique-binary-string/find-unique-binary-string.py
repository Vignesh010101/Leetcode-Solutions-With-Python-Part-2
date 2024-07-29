class Solution:
    def findDifferentBinaryString(self, x: List[str]) -> str:
        t,i,x=len(x[0]),0,sorted([int(j,2) for j in x])
        while i<len(x) and i==x[i]: i+=1
        return "0"*(t-len(bin(i))+2)+bin(i)[2:]