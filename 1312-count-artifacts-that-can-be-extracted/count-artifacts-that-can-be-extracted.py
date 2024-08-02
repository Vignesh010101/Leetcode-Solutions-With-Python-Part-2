class Solution:
    def digArtifacts(self, n: int, artifact: List[List[int]], dig: List[List[int]]) -> int:
        dig_set = set()
        for i in dig:
            dig_set.add(tuple(i))
            
        count = 0
        for afact in artifact:
            flag = True
            r1,c1,r2,c2 = afact
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    if (i,j) not in dig_set:
                        flag = False
                        break
                        
            if(flag == True):
                count += 1
                
        return count