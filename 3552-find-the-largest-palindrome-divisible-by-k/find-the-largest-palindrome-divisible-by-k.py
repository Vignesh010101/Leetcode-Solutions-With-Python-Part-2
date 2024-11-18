class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:

        ans = ['9'] * n
        mid = n//2

        if k in {1, 3, 9} :
            return ''.join(ans)

        if k == 2 :
            ans[0] = ans[~0] = '8'
            return ''.join(ans)

        if k == 4 :
            if n < 4: return '8' * n
            else    : ans[:2] = ans[-2:] = '88'
            return ''.join(ans)

        if k == 5 :
            ans[0] = ans[~0] = '5'
            return ''.join(ans)

        if k == 6 : 
            if n  < 3: return '6'* n
            ans[0] = ans[~0] = '8'
            if n%2: ans[mid] = '8'
            else: ans[mid] = ans[~mid] = '7'
            return ''.join(ans)
            
# --------------- sevens ------------------
        if k == 7 :
            if n < 3: 
                return '7' * n

            mod12 = n %12
            if mod12 in {1,2,4,5}:
                ans[mid] = ans[~mid] = '7'
            if mod12 == 3:
                ans[mid] = '5'    
            if mod12 in {7,8,10,11}:
                ans[mid] = ans[~mid] = '4'
            if mod12 == 9:
                ans[mid] = '6'

            # mod12 = 6 or 12 remain ['9'] * n

            return ''.join(ans)
# ----------------------------------------            

        if k == 8 :
            if n < 6: return '8' * n
            ans[:3] = ans[-3:] = '888' 
            return ''.join(ans)  