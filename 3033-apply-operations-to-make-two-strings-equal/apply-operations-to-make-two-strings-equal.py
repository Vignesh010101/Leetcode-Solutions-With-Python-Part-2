class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = []
        ret = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        if len(diff) & 1: return -1
        
        @cache
        def helper(l, r):
            if l > r: return 0
            ret = min(diff[l+1]-diff[l] + helper(l+2, r), diff[r]-diff[r-1] + helper(l, r-2), x + helper(l+1, r-1))
            return ret
        return helper(0, len(diff)-1)
        
        
        