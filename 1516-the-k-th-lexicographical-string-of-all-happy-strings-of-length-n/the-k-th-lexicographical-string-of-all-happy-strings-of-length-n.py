class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        d = {'a':'bc','b':'ac','c':'ab'}              

        div,r = divmod(k-1,2**(n-1))                    

        if div > 2: return ''
        prev = ans = 'abc'[div]                        
   
        r = list(map(int,bin(r)[2:].rjust(n-1,'0')))    
  
        for i in range(n-1):                           
            prev = d[prev][r[i]]                        
            ans+= prev                                  
        return ans                                    