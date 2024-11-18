from sortedcontainers import SortedList

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = SortedList(range(n))
        ans = []
        for u, v in queries: 
            lo = graph.bisect_right(u)
            hi = graph.bisect_left(v)
            for _ in range(lo, hi): 
                graph.pop(lo)
            ans.append(len(graph)-1)
        return ans 