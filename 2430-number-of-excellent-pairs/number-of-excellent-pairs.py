class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        hamming = sorted([num.bit_count() for num in set(nums)])
        ans = 0
        for h in hamming:
            ans += len(hamming) - bisect.bisect_left(hamming, k - h)
        return ans