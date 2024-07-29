class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sm = mean * (n + len(rolls)) - sum(rolls)
        if sm > n * 6 or sm < n:
            return []
        ans = [sm // n] * n
        lo = sm % n
        for i in range(lo):
            ans[i] += 1
        return ans