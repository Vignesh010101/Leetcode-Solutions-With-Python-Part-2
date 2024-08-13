class Solution:
    def maxNumOfMarkedIndices(self, a: List[int]) -> int:
        return (bisect_left(range(len(a)//2+1),1,key=lambda k,a=sorted(a):1^all(2*p<=q for p,q in zip(a[:k],a[-k:])))-1)*2