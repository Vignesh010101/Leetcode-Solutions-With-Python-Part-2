def f(u, d):
    return u + (u - 1) // (d - 1)


class Solution:
    def minimizeSet(self, d1: int, d2: int, u1: int, u2: int) -> int:
        return max(f(u1, d1), f(u2, d2), f(u1 + u2, math.lcm(d1, d2)))