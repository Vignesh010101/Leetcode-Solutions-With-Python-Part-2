class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        dp=[maxsize]*(max(max(forbidden),x)+a+b+1)
        visited=[False]*(max(max(forbidden),x)+a+b+1)
        for f in forbidden:
            dp[f]=-1
        dp[0]=0
        qu=deque([0])
        while qu:
            id=qu.popleft()
            if id==x:
                return dp[id]
            fow=id+a
            back=id-b
            if fow<len(dp) and dp[id]+1<dp[fow] and not visited[fow]:
                dp[fow]=dp[id]+1
                qu.append(fow)
                visited[fow]=True
            if back>=0 and dp[back]>=0:
                dp[back]=min(dp[back],dp[id]+1)
                fow=back+a
                if fow<len(dp) and dp[id]+2<dp[fow] and not visited[fow]:
                    dp[fow]=dp[id]+2
                    qu.append(fow)
                    visited[fow]=True
            visited[id]=False
        return -1 if dp[x]==maxsize else dp[x]