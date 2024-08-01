class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        mx, n = 0, len(beans)
        for i, bean in enumerate(sorted(beans)):
            mx = max(mx, bean * (n - i))
        return sum(beans) - mx        