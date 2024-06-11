class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        splits = 0
        
        for idx in reversed(range(1, N)):
            left, curr = nums[idx - 1], nums[idx]
            
            if left > curr:
                quotient = left // curr
                remainder = left % curr
                
                if remainder == 0:
                    nums[idx - 1] = curr
                    splits += quotient - 1
                else:
                    nums[idx - 1] = left // (quotient + 1)
                    splits += quotient
        
        return splits