class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        
        diff =[]
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)
        
        m = len(diff)
        if m %2 != 0:
            return -1
        @cache
        def minCostUpTo(i:int):
            if i == 0:
                return x/2
            if i == -1:
                return 0
            return min((minCostUpTo(i-1)+x/2), (minCostUpTo(i-2)+ diff[i]-diff[i-1]))
        
        return int(minCostUpTo(len(diff)-1))