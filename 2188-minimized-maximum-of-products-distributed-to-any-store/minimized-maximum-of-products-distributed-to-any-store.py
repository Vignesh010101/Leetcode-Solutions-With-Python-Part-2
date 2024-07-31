class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        quantities = Counter(quantities)
        def feasible(thresh):
            return sum([ceil(q/thresh) * c for q, c in quantities.items()]) <= n
        
        l, r = 1, max(quantities)
        while l < r:
            m = l + (r-l) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l