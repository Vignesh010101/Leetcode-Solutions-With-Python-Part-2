class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        pad = lambda x: x + [(None, 0)]*(2-len(x))
        even = pad(Counter(nums[::2]).most_common(2))
        odd = pad(Counter(nums[1::2]).most_common(2))
        return len(nums) - (max(even[0][1] + odd[1][1], even[1][1] + odd[0][1]) if even[0][0] == odd[0][0] else even[0][1] + odd[0][1])