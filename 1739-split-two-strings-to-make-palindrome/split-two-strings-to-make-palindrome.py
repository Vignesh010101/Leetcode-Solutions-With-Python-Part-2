class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def q(a,b):
            for e,(c,d) in enumerate(zip(q:=a[:(p:=len(a)//2)][::-1],a[-p:])):
                if c!=d:return q[e:]==b[e-p:] or b[:p-e][::-1]==a[e-p:]
            return 1
        return q(a,b)or q(b,a)