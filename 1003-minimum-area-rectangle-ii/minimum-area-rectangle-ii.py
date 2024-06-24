from itertools import combinations

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        x, y = 0, 1
        vec = lambda p, q: [q[x]-p[x], q[y]-p[y]]
        area = lambda p,q: p[x]*q[y] - p[y]*q[x]
        dist = lambda p,q: (p[x]-q[x])**2 + (p[y]-q[y])**2
        mid_to_diagonals = defaultdict(list)
        for p,q in combinations(points, 2):
            key = p[x] + q[x], p[y] + q[y]
            mid_to_diagonals[key].append((p,q))
        res = float('inf')
        for group in mid_to_diagonals.values():
            for (a,b), (c,d) in combinations(group, 2):
                if dist(a,b) == dist(c,d):
                    res = min(res, abs(area(vec(a,b), vec(a,d))))
        return res if res != float('inf') else 0