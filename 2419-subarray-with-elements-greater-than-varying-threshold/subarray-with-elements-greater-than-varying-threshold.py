class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
							
        nums.append(0)
        stack = deque()

        for idx in range(len(nums)):

            while stack and nums[idx] <= nums[stack[-1]]:           
                n = nums[stack.pop()]                               
                k = idx if not stack else idx - stack[-1] -1        
                if n > threshold //k: return k
            stack.append(idx)

        return -1