class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        lo, hi = 0, 10**5
        while lo < hi: 
            mid = lo + hi >> 1
            if 2*mid*(mid+1)*(2*mid+1) < neededApples: lo = mid + 1
            else: hi = mid
        return 8*lo