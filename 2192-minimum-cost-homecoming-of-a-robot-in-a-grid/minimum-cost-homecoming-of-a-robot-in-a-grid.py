class Solution:
    def minCost(self, sp: List[int], hp: List[int], rc: List[int], cc: List[int]) -> int:
        return (sum(cc[hp[1]:sp[1]]) if  hp[1]<sp[1] else sum(cc[sp[1]+1:hp[1]+1])) + (sum(rc[hp[0]:sp[0]])  if hp[0]<sp[0] else sum(rc[sp[0]+1:hp[0]+1]))