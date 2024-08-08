# using itertools.groupby, 704 ms

from itertools import groupby

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        max_value = max(nums)
        for elem, it in groupby(nums):
            if elem == max_value:
                length = sum(1 for _ in it)
                result = max(result, length)
        return result