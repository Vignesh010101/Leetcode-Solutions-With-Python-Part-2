class Solution:
    def minGroups(self, I: List[List[int]]) -> int:
        N = len(I)
        S, E = [], []
        for s, e in I:
            S.append(s)
            E.append(e)
        S.sort()
        E.sort()

        eIdx = 0
        res = 0
        for sIdx in range(N):
            if S[sIdx] > E[eIdx]:
                eIdx += 1
            else:
                res += 1
        return res