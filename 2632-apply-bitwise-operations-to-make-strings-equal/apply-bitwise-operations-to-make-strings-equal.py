class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        target = list(set(target))
        s = list(set(s))

        if target == s: # 1st condition
            return True
        elif len(target) == len(s): # 2nd condition
            return False
        elif s == ['0'] or target == ['0']: # 3rd condition
            return False
        else:
            return True