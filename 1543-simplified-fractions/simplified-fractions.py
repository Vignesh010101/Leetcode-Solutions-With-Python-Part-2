class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        vy={}
        res=[]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i/j not in vy:
                    vy[i/j]=1
                    res.append(f"{i}/{j}")

        return res