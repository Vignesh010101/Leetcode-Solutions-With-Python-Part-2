class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        return (m:=1) and sum((d<m,m:=max(m,d))[0] for _,d in sorted(p,key=lambda q:(-q[0],q[1])))