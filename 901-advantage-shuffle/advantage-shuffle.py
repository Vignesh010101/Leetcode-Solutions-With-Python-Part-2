class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        I, res, _ = deque(sorted(range(len(nums2)),key = lambda idx: nums2[idx])), [-1] * len(nums1), nums1.sort()
        for boy in nums1:
            if boy > nums2[I[0]]: res[I.popleft()] = boy
            else: res[I.pop()] = boy
        return res