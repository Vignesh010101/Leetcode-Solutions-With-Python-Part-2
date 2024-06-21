class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        degree = Counter(edges)
        kahn = set()
        queue = deque()
        for x in range(n): 
            if degree[x] == 0: queue.append(x)
        while queue: 
            x = queue.popleft()
            kahn.add(x)
            x = edges[x]
            degree[x] -= 1
            if degree[x] == 0: queue.append(x)
        ans = [0]*n 
        for x in set(range(n)) - kahn: 
            if ans[x] == 0: 
                vals = []
                while not vals or x != vals[0]: 
                    vals.append(x)
                    x = edges[x]
                for x in vals: ans[x] = len(vals)
        for x in kahn: 
            stack = []
            while ans[x] == 0: 
                stack.append(x)
                x = edges[x]
            while stack: 
                ans[stack[-1]] = 1+ans[x]
                x = stack.pop()
        return ans 