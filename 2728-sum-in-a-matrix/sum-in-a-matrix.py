class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        res = 0
        n,m = len(nums),len(nums[0])
        for i in range(m):
            curr = -1
            for j in range(n):
                curr = max(curr,nums[j][i])
            res += curr
        return res