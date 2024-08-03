class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
            for i in range(len(nums)-1, -1, -1):
                prev = nums[i]
                for j in range(i-1, -1, -1):
                    prev, nums[j] = nums[j], (nums[j] + prev) % 10

            return nums[0]