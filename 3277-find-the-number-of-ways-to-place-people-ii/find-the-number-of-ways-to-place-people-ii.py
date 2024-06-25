class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:(x[0], -x[1]))
        cnt = 0
        n = len(points)
        
        for p1 in range(n):
            
            i, j = points[p1]
            lo = -float("inf")
            
            for p2 in range(p1 + 1, n):  
                x, y = points[p2]
                
                if y <= lo:
                    continue
                    
                if j >= y:
                    lo = max(lo, y)
                    cnt += 1
        return cnt
        