class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res=1
        mid=(1<<(n-1))

        while k>1:
            if k==mid: return str(res)
            if k>mid:
                k=2*mid-k
                res^=1
            mid>>=1
        
        return str(res^1)