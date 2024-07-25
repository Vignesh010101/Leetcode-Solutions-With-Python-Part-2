class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        if sum(nums)==goal:
            return 0
        x=goal-sum(nums)
        if abs(x)<limit:
            return 1
        count=0
        count+=math.ceil(abs(x)/limit)
        return count