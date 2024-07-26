class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)

        if n.startswith('-'):
            return '-' + self.minimize(n[1:], x)

        return self.maximize(n, x)

    @staticmethod
    def maximize(num: str, x: str) -> str:
        for i, d in enumerate(num):
            if x > d:
                return num[:i] + x + num[i:]

        return num + x

    @staticmethod
    def minimize(num: str, x: str) -> str:
        for i, d in enumerate(num):
            if x < d:
                return num[:i] + x + num[i:]

        return num + x