class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        ps = [0]
        stack = [-1]
        nums.append(0)
        res = 0
        
        for i in range(len(nums)):
            while nums[stack[-1]] > nums[i]:
                min_val = nums[stack.pop()]
                range_sum = ps[i] - ps[stack[-1] + 1]
                res = max(res, range_sum * min_val)
            stack.append(i)
            ps.append(ps[-1] + nums[i])
        return res % mod