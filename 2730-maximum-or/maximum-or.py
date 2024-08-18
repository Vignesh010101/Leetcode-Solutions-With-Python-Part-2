class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        suffix_stack = [0]
        for elem in reversed(nums):
            suffix_stack.append(suffix_stack[-1] | elem)
        suffix_stack.pop()
        
        prefix = result = 0
        for elem in nums:
            current = prefix | suffix_stack.pop() | elem << k
            result = max(result, current)
            prefix |= elem
        return result