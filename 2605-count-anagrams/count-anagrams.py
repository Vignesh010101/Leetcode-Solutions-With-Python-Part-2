class Solution:
    def countAnagrams(self, s: str) -> int:
        words, M, mul, fact = s.split(), 1000000007, lambda a, b: a*b % M, lambda n: functools.reduce(mul, range(2, n+1), 1)
        denom = functools.reduce(mul, (fact(count) for w in words for count in collections.Counter(w).values()), 1)
        return mul(functools.reduce(lambda t, w: mul(t, fact(len(w))), words, 1), pow(denom, -1, M))
        