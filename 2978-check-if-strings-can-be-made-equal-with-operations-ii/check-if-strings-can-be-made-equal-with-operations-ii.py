class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        s1e = Counter(s1[::2])
        s2e = Counter(s2[::2])
        s1o = Counter(s1[1::2])
        s2o = Counter(s2[1::2])
        return s1e == s2e and s1o == s2o