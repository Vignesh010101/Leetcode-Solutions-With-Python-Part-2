class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        obs = set(map(tuple,obstacles))
        x,y, dx,dy, ans = 0,0, 0,1, 0

        for c in commands:

            if c < 0 :
                dx, dy = (dy, -dx) if c+2 else (-dy, dx)  
    
            else:
                for _ in range(c):

                    xx, yy = x+dx, y+dy
                    
                    if (xx, yy) in obs: break
                    x, y = xx, yy

            ans = max(ans, x*x + y*y)

        return ans