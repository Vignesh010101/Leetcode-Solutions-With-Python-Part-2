class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0]) # dimensions 
        queue = [(i, j) for i in range(m) for j in range(n) if isWater[i][j]]
        
        ht = 0
        ans = [[0]*n for _ in range(m)]
        seen = set(queue)
        
        while queue: 
            newq = []
            for i, j in queue: 
                ans[i][j] = ht
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen: 
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ht += 1
        return ans 