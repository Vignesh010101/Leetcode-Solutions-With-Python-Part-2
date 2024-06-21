class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        low = [int(c) for c in low]
        high = [int(c) for c in high]
        nl, nh = len(low), len(high)
        MOD = 1_000_000_007
        
        @cache
        def dp(i, prev, lt, typ):
            if typ == 'L':
                n = nl
                arr = low
            else:
                n = nh
                arr = high
            if i == n:
                return 1
            res = 0
            if prev == -1:
                for v in range(10):
                    res = (res + dp(i + 1, v if v else -1, True, typ)) % MOD
            else:
                for v in prev + 1, prev - 1:
                    if 0 <= v < 10:
                        if not lt and v > arr[i]:
                            continue
                        res = (res + dp(i + 1, v, lt or v < arr[i], typ)) % MOD
            return res
        
        xl = 0
        for v in range(low[0] + 1):
            xl = (xl + dp(1, v if v else -1, v < low[0], 'L')) % MOD
                
        xh = 0
        for v in range(high[0] + 1):
            xh = (xh + dp(1, v if v else -1, v < high[0], 'H')) % MOD
        
        extra = 0
        if len(low) == 1 or all(abs(low[i] - low[i + 1]) == 1 for i in range(nl - 1)):
            extra = 1
        return (xh - xl + extra) % MOD
        