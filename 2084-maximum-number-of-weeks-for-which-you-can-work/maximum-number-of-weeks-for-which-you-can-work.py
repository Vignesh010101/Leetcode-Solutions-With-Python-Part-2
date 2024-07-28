class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _sum, _max = sum(milestones), max(milestones)
        if _sum - _max >= _max:  
            return _sum
        return 2 * (_sum - _max) + 1  