class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total_sum = 0
        
        for row in nums:
            row.sort()
        
        for i in range(len(nums[0])):
            maxi = 0
            for j in range(len(nums)):
                maxi = max(nums[j][i], maxi)
            total_sum += maxi
        
        return total_sum
