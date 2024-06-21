class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        nums2_sorted = sorted(nums2)
        nums2_idx_map = dict(zip(nums2_sorted, range(n)))
        ab = sorted([(a, b) for a, b in zip(nums1, nums2)], reverse=True)
        queries = sorted([(x, y, i) for i, (x, y) in enumerate(queries)], reverse=True)
        tree = SegmentTree(n)
        res = [-1] * len(queries)
        j = 0
        for x, y, i in queries:
            while j < n and ab[j][0] >= x:
                tree.set(nums2_idx_map[ab[j][1]], ab[j][0] + ab[j][1])
                j += 1
            y_idx = bisect.bisect_left(nums2_sorted, y)
            if y_idx == n:
                continue
            else:
                res[i] = tree.max(y_idx, n)
        return res

    
class SegmentTree:
    def __init__(self, n):
        self.size = 1 << (n - 1).bit_length()
        self.data = [-1] * (2 * self.size)

    def set(self, i, x):
        i += self.size
        if self.data[i] >= x:
            return
        self.data[i] = x
        while i > 1:
            self.data[i >> 1] = max(self.data[i], self.data[i ^ 1])
            i >>= 1

    def max(self, l, r):
        l += self.size
        r += self.size
        s = -1
        while l < r:
            if l & 1:
                s = max(s, self.data[l])
                l += 1
            if r & 1:
                s = max(s, self.data[r - 1])
            l >>= 1
            r >>= 1
        return s
        