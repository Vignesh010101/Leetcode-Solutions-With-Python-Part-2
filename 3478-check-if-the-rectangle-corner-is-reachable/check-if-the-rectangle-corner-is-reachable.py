class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        vals = []
        for xi, yi, ri in circles: 
            if xi**2 + yi**2 <= ri**2: return False 
            if (X-xi)**2 + (Y-yi)**2 <= ri**2: return False 
            if xi >= X+ri or yi > Y+ri: continue 
            vals.append([xi, yi, ri])
        circles = vals
        
        n = len(circles)
        parent = list(range(n))
        
        def find(p): 
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        for i in range(n): 
            xi, yi, ri = circles[i]
            for j in range(i+1, n): 
                xj, yj, rj = circles[j]
                if (xi-xj)**2 + (yi-yj)**2 <= (ri+rj)**2: 
                    ii = find(i)
                    jj = find(j)
                    parent[ii] = jj 
                    
        group = defaultdict(list)
        for i in range(n): 
            ii = find(i)
            group[ii].append(i)
        
        for grp in group.values(): 
            imax = jmax = -inf
            imin = jmin = inf 
            inside = False
            for i in grp:
                i, j, r = circles[i]
                if 0 <= i <= X or 0 <= j <= Y: inside = True 
                imax = max(imax, i+r)
                jmax = max(jmax, j+r)
                imin = min(imin, i-r)
                jmin = min(jmin, j-r)
            if inside: 
                if imin <= 0 and imax >= X: return False 
                if jmin <= 0 and jmax >= Y: return False 
                if imax >= X and jmax >= Y: return False 
                if imin <= 0 and jmin <= 0: return False 
        return True 