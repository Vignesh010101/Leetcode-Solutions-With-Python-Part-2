class Solution:
    def maximumRows(self, m: List[List[int]], k: int) -> int:
        return (n:=len(m[0])) and max(sum(all(r[c]==0 for c in q) for r in m) for q in combinations([*range(n)],n-k))