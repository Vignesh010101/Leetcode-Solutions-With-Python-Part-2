def euclidean(x):
    return x[0]**2+x[1]**2
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush as push ,heappop as pop
        l,n,h=points,len(points),[]
        size=0
        for i in range(n):
            push(h,(-euclidean(l[i]),l[i]))
            size+=1

            if size>k:
                pop(h)
                size-=1
        
        ans=[i[1] for i in h]
        return ans
        