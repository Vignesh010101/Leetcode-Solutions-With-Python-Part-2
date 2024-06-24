class Solution:
    def isValid(self, s: str) -> bool:
        prev = None
        while s != "" and s != prev:
            prev = s
            s = s.replace("abc", "")
        return s == ""