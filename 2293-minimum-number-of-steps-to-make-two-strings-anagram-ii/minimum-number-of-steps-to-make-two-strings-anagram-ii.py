class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc=Counter(s)
        tc=Counter(t)
        tmp=sc & tc
        tmpsum=sum(tmp.values())
        return len(s)+len(t)-tmpsum-tmpsum