class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def f(upper):
            s = str(upper)
            @cache
            def dfs(i, val, diff, isLimit, isNum):
                if i == len(s):
                    return int(isNum and val == 0 and diff == 0)
                res = 0
                if not isNum: res = dfs(i+1, val, diff, False, False)
                bottom = 0 if isNum else 1
                top = int(s[i]) if isLimit else 9
                for d in range(bottom, top + 1):
                    res += dfs(i+1, (val * 10 + d) % k, diff + d % 2 * 2 - 1, isLimit and d == top, True)
                return res
            return dfs(0, 0, 0, True, False)
        return f(high) - f(low-1)