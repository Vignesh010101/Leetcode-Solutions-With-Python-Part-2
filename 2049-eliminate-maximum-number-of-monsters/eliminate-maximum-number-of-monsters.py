class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)): dist[i]/=speed[i]
        haveToKill = [0 for i in dist]

        for x in dist:

            if ceil(x)<len(dist):

                haveToKill[ceil(x)]+=1 
        for i in range(len(speed)):
            if i>0: haveToKill[i]+=haveToKill[i-1]
            if haveToKill[i]>i: return i
        
        return len(dist)
