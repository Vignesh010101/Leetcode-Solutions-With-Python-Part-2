class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points[0])
        def mySum(row1, row2):
            for i in range(1,n): row1[i] = max(row1[i], row1[i-1] - 1)
            for i in range(n-2, -1, -1): row1[i] = max(row1[i], row1[i+1] - 1)
            return [x+y for x, y in zip(row1, row2)]
        return max(list(reduce(lambda row1, row2: mySum(row1, row2), points[::-1])))