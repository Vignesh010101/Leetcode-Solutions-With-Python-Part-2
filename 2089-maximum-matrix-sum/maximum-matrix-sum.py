class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = tuple(chain(*matrix))
        hasOddNeg = reduce(operator.xor, map(lambda x: x < 0, arr))
        absArr = tuple(map(abs, arr))
        res = sum(absArr) - 2 * hasOddNeg * min(absArr)
        return res