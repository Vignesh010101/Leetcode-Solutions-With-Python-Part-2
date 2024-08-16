class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        aug = [(q, i) for i, q in enumerate(queries)]
        aug.sort()
        total = sum(nums)
        prefix = 0
        k = 0
        ans = [0] * len(queries)
        for q, i in aug:
            while k < len(nums) and nums[k] < q:
                prefix += nums[k]
                k += 1
            ans[i] = total - 2 * prefix + q * (2 * k - len(nums))
        return ans       