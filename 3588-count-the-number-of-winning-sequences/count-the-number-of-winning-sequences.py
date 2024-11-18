class Solution:
    def countWinningSequences(self, s: str) -> int:
        wins = {"W": "F", "E": "W", "F": "E"}
        loses = {"F": "W", "W": "E", "E": "F"}

        @cache
        def dp(i, prev, point):
            if i == len(s):
                return int(point > 0)
            res = 0
            for c in "WEF":
                if c != prev:
                    res += dp(i + 1, c, point + int(s[i] == wins[c]) - int(s[i] == loses[c]))
                    res %= 1_000_000_007
            return res
        
        return dp(0, '', 0)