class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod, pre_sum = int(1e9+7), [nums[0]]
        for num in nums[1:]:
            pre_sum.append(pre_sum[-1] + num)
        ans, n = 0, len(nums)
        for i in range(n):
            prev = pre_sum[i]
            if prev * 3 > pre_sum[-1]: break
            j = bisect.bisect_left(pre_sum, prev * 2, i+1)
            middle = (prev + pre_sum[-1]) // 2
            k = bisect.bisect_right(pre_sum, middle, j+1)
            if k-1 >= n or pre_sum[k-1] > middle: continue
            ans = (ans + min(k, n - 1) - j) % mod
        return ans