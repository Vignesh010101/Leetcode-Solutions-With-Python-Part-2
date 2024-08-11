class Solution:
    def monkeyMove(self, n: int) -> int:
        n=bin(n)[2:]
        n=n[::-1] 
        y,a=1,2
        m=(10**9)+7
        for i in n:
            if i=='1':
                y=(y*a)%m
            a=(a*a)%m 
        return (y-2)%m        