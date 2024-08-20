class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for start, end in zip(moveFrom, moveTo):
            nums.discard(start)
            nums.add(end)
        
        return sorted(nums)