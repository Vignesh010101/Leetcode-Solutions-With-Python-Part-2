class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        res = 0
        unsorted = set(range(m - 1))
        for j in range(n):
            if any(strs[i][j] > strs[i+1][j] for i in unsorted):
                res += 1
            else:
                unsorted -= {i for i in unsorted if strs[i][j] < strs[i+1][j]}
        return res