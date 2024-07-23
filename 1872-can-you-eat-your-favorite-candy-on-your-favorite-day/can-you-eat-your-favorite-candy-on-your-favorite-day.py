class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        A = [0] + list(accumulate(candiesCount))
        res = []
        for type, day, cap in queries:
            to_be_eaten = A[type] + 1
            res.append(to_be_eaten <= ((day + 1) * cap) and A[type + 1] > day)
        return res