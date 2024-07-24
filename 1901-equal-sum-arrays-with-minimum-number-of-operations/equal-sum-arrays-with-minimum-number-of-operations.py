class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        M = len(nums1)
        N = len(nums2)

        if 6 * M < N or 6 * N < M: 
            return -1

        S1 = sum(nums1)
        S2 = sum(nums2)

        rem = abs(S1 - S2)
        if S1 > S2: 
            nums1, nums2 = nums2, nums1

        diffs = [0] * 6
        for n in nums1:
            diffs[6 - n] += 1

        for n in nums2:
            diffs[n - 1] += 1

        ans = 0
        while rem:
            count = diffs.pop()
            diff = len(diffs)

            if count * diff >= rem:
                ans += (rem + diff - 1) // diff
                return ans
            else:
                ans += count
                rem -= count * diff

        assert rem == 0
        return ans
