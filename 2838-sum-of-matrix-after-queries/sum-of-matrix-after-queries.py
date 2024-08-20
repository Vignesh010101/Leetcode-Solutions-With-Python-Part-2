class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0
        cntR, cntC = n, n
        R = [True] * n
        C = [True] * n
        for t, i, v in queries[::-1]:
            if t == 0 and R[i]:
                ans += v * cntC
                cntR -= 1
                R[i] = False
            elif t == 1 and C[i]:
                ans += v * cntR
                cntC -= 1
                C[i] = False
        return ans