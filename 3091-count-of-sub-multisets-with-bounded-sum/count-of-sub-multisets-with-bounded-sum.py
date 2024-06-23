class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        N = 0
        for c  in nums:
            N+=c
        
        freq = [0]*(N+1)
        for c in nums:
            freq[c]+=1

            
        compressed =[]
        
        for i in range(1,N+1):
            if freq[i] > 0 :
                compressed.append((i, freq[i]))

        
        dp = [0]*(N+1)
        dp[0] = freq[0]+1
        mod = 10**9 + 7
        
        for w,k in compressed:
            ndp = dp.copy()
            
            for p in range(w):
                sum = 0
                
                multiple = p
                count = 0
                while multiple <=N:
                    if (count > k):
                        sum -= dp[multiple - (w * count)]
                        count-=1

                    ndp[multiple] += sum
                    sum += dp[multiple]
                    multiple+=w
                    count+=1

            dp,ndp = (ndp,dp)
        
        ans = 0
        for i in range(l,min(N+1,r+1)):
            ans+=dp[i]
            ans%=mod
            
        return ans
        
        