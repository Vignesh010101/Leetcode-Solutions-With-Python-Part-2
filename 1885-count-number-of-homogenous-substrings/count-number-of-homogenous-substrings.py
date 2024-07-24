class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum((vy:=len(list(substr)))*(vy+1)//2 for _,substr in groupby(s))%(10**9+7)