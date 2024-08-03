class Solution:
    def minimizeResult(self, expression: str) -> str:

        def eval_expr(l,li,ri):
            ai=1
            if li!=0:
                l.insert(li,'*')
                ai+=1
            if ri!=len(l)-ai:
                l.insert(ri+ai,'*')
            return eval(''.join(l))

        pi=expression.index('+')
        length=len(expression)
        res_sum,res_s=float('inf'),None
        for i in range(pi):
            for j in range(pi+2,length+1):
                l=list(expression)
                l.insert(i,'(')
                l.insert(j+1,')')
                t=eval_expr(l,i,j+1)
                if t<res_sum:
                    res_sum=t
                    res_s=''.join([c for c in l if c!='*'])
        return res_s