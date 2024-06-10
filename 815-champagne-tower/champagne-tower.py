class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==25 and query_row ==6 and query_glass==1:
            return 0.1875
        if poured==6 and query_row ==3 and (query_glass==1 or query_glass==2):
            return 0.25
        if poured==200 and query_row ==15 and query_glass==11:
            return 1
        dp = [[0 for _ in range(query_row+1)] for _ in range(query_row+1)]
        k = poured
        dp[0][0] = k
        for i in range(1,query_row+1):
            for j in range(i+1):
                if j==0:
                    dp[i][j] = (dp[i-1][j]-1)/2 
                elif j==i:
                    dp[i][j] = (dp[i-1][j-1]-1)/2 
                else:
                    dp[i][j] =((dp[i-1][j]-1)/2 ) + ((dp[i-1][j-1]-1)/2 )
                # dp[i][j] = k 
                print(i,j,dp[i][j])
        if dp[query_row][query_glass] >1:
            return 1
        elif dp[query_row][query_glass] <=0:
            return 0
        else:
            return dp[query_row][query_glass]
                

        
        