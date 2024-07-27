class Solution:
    def sumGame(self, num: str) -> bool:                    
        n = len(num)//2                                     
        num = [9 if ch=='?' else 2*int(ch) for ch in num]  
        return  sum(num[:n]) != sum(num[n:])               