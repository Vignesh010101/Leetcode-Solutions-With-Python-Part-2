class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res=[]
        for x,y in queries:
            ans=1
            while x!=y:
                if x>y:
                    x//=2
                else:
                    y//=2
                ans+=1
            res.append(ans)
        
        return res