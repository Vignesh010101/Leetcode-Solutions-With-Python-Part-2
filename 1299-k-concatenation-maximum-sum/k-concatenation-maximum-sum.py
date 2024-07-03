class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
       
        acc = list(accumulate(chain(*[arr]*(2-(k==1))),
                   lambda x,y: max(0,x+y), initial = 0))
       
        return (max(acc) + (k-2)*sum(arr)*(sum(arr)>0)*(k>1))%1000000007