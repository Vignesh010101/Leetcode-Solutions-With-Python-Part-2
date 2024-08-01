class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for k, v in freq.items():
            if (v == 1) and (k + 1 not in freq) and (k - 1 not in freq):
                res.append(k)

        return res