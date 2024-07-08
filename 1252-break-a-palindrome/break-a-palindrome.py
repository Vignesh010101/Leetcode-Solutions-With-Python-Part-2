class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n=len(palindrome)
        if n==1:
            return ""
        st=""
        for i in range(n):
            if palindrome[i]!='a':
                st+='a'
                st+=palindrome[i+1:]
                if st!=st[::-1]:
                    return st
                else: break
            st+=palindrome[i]
        return palindrome[:-1]+'b'
        n=len(palindrome)
        
        if n==1: return ''
        
        for i in range(n//2):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'
            