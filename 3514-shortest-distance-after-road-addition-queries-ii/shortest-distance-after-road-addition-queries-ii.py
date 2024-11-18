class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        jump = list(range(1, n))
        n -= 1
        for u, v in queries: 
            while jump[u] < v: 
                jump[u], u = v, jump[u]
                n -= 1
            ans.append(n)
        return ans 