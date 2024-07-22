class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [] # (increasing) mono-stack 
        for i, x in enumerate(nums): 
            while stack and stack[-1] > x and len(stack) + len(nums) - i > k: stack.pop()
            if len(stack) < k: stack.append(x)
        return stack 