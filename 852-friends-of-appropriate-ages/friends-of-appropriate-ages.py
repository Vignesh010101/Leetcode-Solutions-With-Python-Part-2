class Solution:
    def numFriendRequests(self, nums: List[int]) -> int:
        res = 0
        freq = Counter(nums)
        for x in freq.keys():
            for y in freq.keys():
                if freq[x] and freq[y] and x >= y > 0.5 * x + 7:
                    res += (freq[x] - (x == y)) * freq[y]
        return res