class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def dfs(N,num):
            if N==0:
               res.append(num)
               return
            
            last_dig = num%10

            next_digs = set([last_dig+k, last_dig-k])

            for next_dig in next_digs:
                if 0<= next_dig<10:
                    new_num = num*10+next_dig
                    dfs(N-1, new_num)
            
        for num in range(1, 10):
            dfs(n-1, num)
        
        return res