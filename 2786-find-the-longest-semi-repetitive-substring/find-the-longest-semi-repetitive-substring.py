class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        rep=0
        m=0
        res=1
        left=0
        flag=True
        for right in range(1,len(s)):
            if s[right-1]==s[right]:
                if not rep:
                    if m<res:
                        m=res
                    res=right-left+1
                    left=right
                    rep=1
                else:
                    if m<res:
                        m=res
                    res=right-left+1
                    left=right
            else:
                res+=1
        return max(m,res)
        