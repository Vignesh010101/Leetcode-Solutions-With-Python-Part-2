class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        A=bin(a)[2:]
        B=bin(b)[2:]
        C=bin(c)[2:]
        count=0
        lenAlenB=max(len(A),len(B))
        lenC=max(lenAlenB,len(C))
        i=0
        A=int(bin(a)[2:])
        B=int(bin(b)[2:])
        C=int(bin(c)[2:])
        while i< lenC:
            digitA=A%10 
            digitB=B%10
            digitC=C%10 
            if int(digitA or digitB) != digitC:
                if digitC==1:
                    count=count+1
                else:
                    count=count+digitA + digitB 
            i=i+1
            A=A//10
            B=B//10
            C=C//10
        return count