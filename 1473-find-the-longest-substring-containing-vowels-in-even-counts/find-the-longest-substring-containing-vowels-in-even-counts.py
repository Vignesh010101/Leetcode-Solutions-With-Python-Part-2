class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
                                                
        d = defaultdict(int)
        v = {'a':0,'e':1,'i':2,'o':3,'u':4,}        
        n, ans, d[0] = 0, 0, -1                    
                                                   
        for i, ch in enumerate(s):                 
            if ch in 'aeiou': n ^= (1<<v[ch])      
            if n in d: ans = max(ans, i - d[n])     
            else:      d[n] = i                     
        return ans                                  