class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l=[0]*128
        for chr in s:
            i=ord(chr)
            l[i]=max(l[i-k:i+k+1])+1
        
        return max(l)