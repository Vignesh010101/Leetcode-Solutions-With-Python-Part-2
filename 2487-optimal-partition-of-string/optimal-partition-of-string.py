class Solution:
    def partitionString(self, s: str) -> int:
        set1=set(())
        res=0
        for i in range(len(s)):
            if s[i] in set1:
                set1.clear()
                res+=1
            set1.add(s[i])
        res+=1
        return res