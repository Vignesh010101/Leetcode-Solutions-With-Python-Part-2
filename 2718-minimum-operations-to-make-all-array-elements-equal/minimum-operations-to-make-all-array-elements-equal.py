class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        cumSum = [0] * len(nums)
        res = []

        cumSum[0] = nums[0]
        for i in range(1, len(nums)):
            cumSum[i] += cumSum[i-1] + nums[i]
        
        for q in queries:
            pos = bisect_right(nums, q)
            if pos-1 >= 0 and nums[pos-1] == q:
                pos = pos - 1
            if pos == 0:
                res.append(abs(cumSum[len(nums) - 1] - (q * len(nums))))
            else:
                s = abs((cumSum[pos - 1] - (q * pos)))
                f = (cumSum[len(nums) - 1] - cumSum[pos - 1]) - (q * (len(nums) - pos))
                res.append(s+f)
        
        return res