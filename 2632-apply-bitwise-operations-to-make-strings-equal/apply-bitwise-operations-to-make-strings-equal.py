class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if '1' in target and '1' in s or target==s:
            return True