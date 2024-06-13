class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n, s = len(nums), sum(nums)
        if n < 2: return 0
        g = [[] for _ in range(n)]
        in_degree = [0 for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
        
        def is_cuttable(f: int) -> bool:
            d, values = in_degree.copy(), nums.copy()
            dq = collections.deque(u for u in range(n) if d[u] == 1)
            while dq:
                u = dq.popleft()
                d[u] = 0
                if values[u] > f: return False
                elif values[u] == f: values[u] = 0
                for v in g[u]:
                    if d[v] == 0: continue
                    d[v] -= 1
                    values[v] += values[u]
                    if d[v] == 1: dq.append(v)
            return True

        factor_nums = [i for i in range(1, s + 1) if s % i == 0]
        for f in factor_nums:
            if is_cuttable(f): return s // f - 1
        
        return 0