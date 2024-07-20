class Solution:
    def minOperations(self, n: int) -> int:
        target = -1
        if n & 1:
            target = ((n // 2) * 2) + 1
        else:
            target = n

        res = 0
        for i in range((n + 1) // 2):
            cal = 2 * i + 1
            res += target - cal

        return res