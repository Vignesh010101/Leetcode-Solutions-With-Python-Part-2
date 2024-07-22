class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        op1 = lambda s: "".join(str((int(c)+a)%10) if i&1 else c for i, c in enumerate(s))
        op2 = lambda s: s[-b:] + s[:-b]
        
        seen = set()
        stack = [s]
        while stack: 
            s = stack.pop()
            seen.add(s)
            if (ss := op1(s)) not in seen: stack.append(ss)
            if (ss := op2(s)) not in seen: stack.append(ss)
        return min(seen)