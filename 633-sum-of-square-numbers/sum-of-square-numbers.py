class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**(1/2))

        while a<=b:
            m=a*a+b*b
            if m==c:
                return True
            if m<c:
                a+=1
            else:
                b-=1
        
        return False