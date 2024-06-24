class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == b:
            return "ab" * a

        x, y = ("a", "b") if a < b else ("b", "a")
        xc, yc = (a, b) if a < b else (b, a)
        n_yyx = min(xc, yc - xc)
        n_yx = min(xc - n_yyx, yc - 2 * n_yyx)
        nx = xc - n_yyx - n_yx
        ny = yc - 2 * n_yyx - n_yx
        return (y + y + x) * n_yyx + (y + x) * n_yx + y * ny + x * nx