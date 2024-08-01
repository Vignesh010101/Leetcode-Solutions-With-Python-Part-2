class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps=0
        while target!=1:
            if target%2==0 and maxDoubles!=0:
                target=target//2
                maxDoubles-=1
            else:
                target-=1
            
            if maxDoubles==0:
                steps=steps+target
                return steps
            steps+=1
        return steps