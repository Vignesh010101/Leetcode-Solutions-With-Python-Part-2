class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, 1000000007) - 2) % 1000000007