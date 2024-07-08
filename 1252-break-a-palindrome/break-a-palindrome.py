class Solution:
    import re
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""

        ret = re.sub(r"[^a]", 'a', palindrome, 1)
        if not self.ispal(ret):
            return ret
			
        ret = re.sub(r"[^b]", 'b', palindrome[::-1], 1)[::-1]
        return ret
        
    def ispal(self, what):
        return what == what[::-1]