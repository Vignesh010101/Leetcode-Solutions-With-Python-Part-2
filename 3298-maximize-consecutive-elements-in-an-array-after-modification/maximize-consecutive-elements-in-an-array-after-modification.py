class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        counts = {}
        for num in nums:
            counts[num + 1] = counts.get(num, 0) + 1
            counts[num] = 1 + counts.get(num - 1, 0)
            
        ans = 0
        for key, value in counts.items():
            ans = max(ans, value)
            
        return ans
            