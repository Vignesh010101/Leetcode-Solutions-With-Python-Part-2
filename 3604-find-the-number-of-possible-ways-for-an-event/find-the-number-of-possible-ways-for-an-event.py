mod = 1_000_000_007

@lru_cache(None)
def stirling2_(n: int, i: int)-> int:
    if not 0 <= i <= n: return 0
    if n == 0: return 1
    return (stirling2_(n - 1, i - 1) + i * stirling2_(n - 1, i)) % mod

@lru_cache(None)
def factorial_(num: int)-> int:
    if num == 0: return 1
    return (num * factorial_(num - 1))% mod

@lru_cache(None)
def comb_(n,i):
    if i == 0: return 1
    return comb_(n,i-1)* (n-i+1) // i   


class Solution:
    def numberOfWays(self, n: int, x: int, y: int, ans = 0) -> int:        
        
        for i in range(1, min(n, x) + 1):

            ans+= (comb_(x, i) * factorial_(i) * stirling2_(n, i) * pow(y, i, mod)) ####
            ans%= mod

        return ans