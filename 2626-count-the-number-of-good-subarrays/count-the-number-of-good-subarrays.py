class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        D = defaultdict(int)
        ans = cnt = l = 0
        for i in A:
            cnt += D[i]
            D[i] += 1
            while cnt >= k:
                D[A[l]] -= 1
                cnt -= D[A[l]]
                l += 1
            ans += l
        return ans