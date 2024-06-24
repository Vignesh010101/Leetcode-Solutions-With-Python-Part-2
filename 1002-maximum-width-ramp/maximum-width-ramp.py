class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        lhs = [0]
        for i, e in enumerate(nums):
            if nums[i] < nums[lhs[-1]]:
                lhs.append(i)
        
        max_width = 0
        j = len(nums)-1
        while lhs:
            i = lhs.pop()
            while j-i > max_width:
                if nums[i] <= nums[j]:
                    max_width = j-i
                    break
                j -= 1
        return max_width