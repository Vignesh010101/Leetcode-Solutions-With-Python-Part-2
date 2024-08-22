class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        new = nums[-1]
        m = 0
        ind = len(nums)-2
        while ind >= 0:
            if nums[ind] <= new:
                new += nums[ind]
                
            else:
                if m < new:
                    m = new
                new = nums[ind]
            ind -= 1
        
        if m < new:
            return new
        else:
            return m

            