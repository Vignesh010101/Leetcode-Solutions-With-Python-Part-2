class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        m = defaultdict(list)
        for x,y in edges:
            if vals[y]>0:
                heapq.heappush(m[x], vals[y])
                if len(m[x])>k: heapq.heappop(m[x])
            if vals[x]>0:
                heapq.heappush(m[y], vals[x])
                if len(m[y])>k: heapq.heappop(m[y])
        return max(vals[i]+sum(m[i]) for i in range(len(vals)))