class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        lm = 0  
        lg = 0  
        lp = 0 
        ans = 0

        for i in range(len(garbage)):
            if "G" in garbage[i]:
                lg = i
            if "P" in garbage[i]:
                lp = i
            if "M" in garbage[i]:
                lm = i
            ans+=len(garbage[i])

        ans+=sum(travel[:lm])+sum(travel[:lg])+sum(travel[:lp])

        return ans
        