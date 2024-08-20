class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:return (4 * x + 2 * z)
        mini = min(x, y)
        return (2 * mini + 2 * (mini + 1) + 2 * z)