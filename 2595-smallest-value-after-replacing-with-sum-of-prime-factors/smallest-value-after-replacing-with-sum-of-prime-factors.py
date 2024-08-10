class Solution:
    def smallestValue(self, n: int) -> int:
        sum = 0 
        c = 2
        org_n = n
        while n > 1:
            if(n % c == 0):
                sum = sum + c
                n = n // c
            else:
                c+=1
        if sum == org_n:
            return org_n
        return self.smallestValue(sum)
      
        
        