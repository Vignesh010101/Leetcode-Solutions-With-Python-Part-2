class Solution:
    def twoEggDrop(self, n: int) -> int:
        ans = ((1+8*n)**0.5 -1)/2
        return math.ceil(ans)
        