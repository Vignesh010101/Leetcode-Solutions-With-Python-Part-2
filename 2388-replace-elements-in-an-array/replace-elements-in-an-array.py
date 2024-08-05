class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {
            elem: index
            for index, elem in enumerate(nums)
        }

        for old, new in operations:
            index = d.pop(old)
            d[new] = index
        
        result = [None] * len(nums)
        for elem, index in d.items():
            result[index] = elem
        return result