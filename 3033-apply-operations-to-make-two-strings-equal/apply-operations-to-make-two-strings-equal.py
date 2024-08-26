class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        
        ones = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ones.append(i)
        
        @cache
        def dp(i, cheat):
            if i == len(ones):
                return 0 if not cheat else inf
            ret = dp(i+1, not cheat) + x / 2
            if i < len(ones)-1:
                pos_a, pos_b = ones[i], ones[i+1]
                ret = min(ret, dp(i+2, cheat)+pos_b-pos_a)
            return ret
        
        ret = dp(0, False)
        return int(ret) if ret != inf else -1