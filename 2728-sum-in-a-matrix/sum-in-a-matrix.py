class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        sorted_array = [sorted(row,reverse=True) for row in nums]
        transposed_array = [list(row) for row in zip(*sorted_array)]
        return sum([max(i) for i in transposed_array])