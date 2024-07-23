class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        d = dict()
        
        @lru_cache(None)
        def dfs(i):
            nonlocal c, d, min_i
            for nei in graph[i]:
                if nei not in d:
                    c[source[nei]] += 1
                    d[nei] = min_i
                    dfs(nei)
        
        for i, num in enumerate(source):
            if i not in d:
                min_i = d[i] = i
                c = collections.defaultdict(int)
                c[num] = 1
                dfs(i)
                d[i] = c
        
        ans = 0
        for i, tar in enumerate(target):
            if isinstance(d[i], int):
                if d[d[i]][tar] > 0:
                    d[d[i]][tar] -= 1
                else:
                    ans += 1
            else:
                if d[i][tar] > 0:
                    d[i][tar] -= 1
                else:
                    ans += 1
        return ans
