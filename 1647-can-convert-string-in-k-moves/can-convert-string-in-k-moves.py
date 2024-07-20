class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t): return False
        dp=[-1]*27
        for a,b in zip(s,t):
            n=ord(b)-ord(a)
            dp[n if n>=0 else 26+n]+=1
        return all([dp[i]<=(k-i)//26 for i in range(1,27)])