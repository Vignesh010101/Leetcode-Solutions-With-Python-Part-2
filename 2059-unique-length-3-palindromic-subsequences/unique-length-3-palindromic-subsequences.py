class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        for i in range(0,26):
            c=chr(i+ord('a'))
            if c in s:
                first=s.index(c)
                last=s.rindex(c)
                if first!=last:
                    u=set()
                    for index in range(first+1,last):
                        u.add(s[index])
                    ans+=len(u)
        return ans                