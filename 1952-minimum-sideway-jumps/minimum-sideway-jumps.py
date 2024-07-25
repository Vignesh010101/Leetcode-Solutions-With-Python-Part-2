class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        frog = 2
        res = 0
        r = 0
        
        while r < len(obstacles):
            l1, l2 = r, r
            
            if r + 1 < len(obstacles) and obstacles[r + 1] == frog:
                res += 1
                
                if frog == 1:
                    f1, f2 = 2, 3
                elif frog == 2:
                    f1, f2 = 1, 3
                else:
                    f1, f2 = 1, 2
                
                o1 = o2 = False
                
                while l1 < len(obstacles) and l2 < len(obstacles) and not (o1 and o2):
                    if obstacles[l1] == f1:
                        o1 = True
                    if obstacles[l2] == f2:
                        o2 = True
                    
                    l1 += 1 if not o1 else 0
                    l2 += 1 if not o2 else 0
                
                frog = f1 if l1 > l2 else f2
                r = max(l1 - 1, l2 - 1)
            else:
                r += 1
        
        return res
