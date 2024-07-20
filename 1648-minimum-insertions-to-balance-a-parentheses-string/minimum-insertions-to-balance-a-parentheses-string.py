class Solution:
    def minInsertions(self, s: str) -> int:
        s=s.replace('))','}')
        missed_bracs=0
        rqrd_ones=0

        for c in s:
            if c=='(':
                rqrd_ones+=2

            else:
                if c==')':
                    missed_bracs+=1
                
                if rqrd_ones:
                    rqrd_ones-=2

                else:
                    missed_bracs+=1
        
        return missed_bracs+rqrd_ones