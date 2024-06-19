class Solution:
       
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        ones=[0]*(n)
        ct=0
        for i in range(n):
            if s[i]=='1':
                ct+=1
            ones[i]=ct
        prev=0
        for i in range(1,n+1):
            if s[i-1]=='0':
                curr=min(prev+1,ones[i-1])
            else:
                curr=min(prev,ones[i-1])
            prev=curr
        return prev