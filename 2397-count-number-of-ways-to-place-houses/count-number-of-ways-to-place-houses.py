size = 10**9 + 7
res = [-1]*(10**4+1)
res[1] = 2
res[2] = 3

def fib(n):
    if res[n]>=0: return res[n]
    l = fib(n-1)
    r = fib(n-2)
    res[n] = (l+r) % size
    return res[n]

class Solution:
    def countHousePlacements(self, n: int) -> int:
        return (fib(n)**2) % size