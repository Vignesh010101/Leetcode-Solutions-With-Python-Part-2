class Solution:
    def numSub(self, s: str) -> int:

        c = 0
        ans = 0
        for item in s:
            if item == '1':
                c += 1
            else:
                ans += c*(c+1)//2
                c = 0
        else:
            ans += c*(c+1)//2

    
        return ans % (10**9+7)