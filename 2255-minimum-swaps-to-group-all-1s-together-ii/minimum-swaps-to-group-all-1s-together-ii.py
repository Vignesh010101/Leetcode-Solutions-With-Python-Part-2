class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt1, n = nums.count(1), len(nums)
        ans = steps = cnt1 - sum(nums[:cnt1])
        for i in range(cnt1, n + cnt1):
            steps += (not nums[i % n]) - (not nums[(i - cnt1) % n])
            ans = min(steps, ans)
        return ans