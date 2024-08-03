class Solution:
    def minimizeResult(self, expression: str) -> str:
        res = {}
        addPos = expression.index('+')
        for i in range(len(expression)):
            if i >= addPos: break
            for j in range(i+1, len(expression)):
                if j <= addPos: continue
                newEx = expression[:i]+'('+expression[i:j+1]+')'+expression[j+1:]
                ans = self.calculate(newEx)
                res[ans] = newEx
        return res[min(res)]
    def str2int(self, arr):
        return int(''.join([str(ch) for ch in arr]))
    def calculate(self, ex):
        digits = []
        mulStack = []
        addStack = []
        i = 0
        L = len(ex)
        while i < L:
            c = ex[i]
            if c.isdigit():
                digits.append(c)
            else:
                if c == '(':
                    if digits:
                        mulStack.append(self.str2int(digits))
                        digits = []
                    subAddStack = []
                    subDigits = []
                    j = i+1
                    while ex[j] != ')':
                        if ex[j].isdigit():
                            subDigits.append(ex[j])
                        else: # +
                            thisNum = self.str2int(subDigits)
                            subAddStack.append(thisNum)
                            subDigits = []
                        j += 1
                    if subDigits:
                        subAddStack.append(self.str2int(subDigits))
                    num = sum(subAddStack)
                    mulStack.append(num)
                    i = j
                elif c == '+':
                    num = 1
                    if digits:
                        num = self.str2int(digits)
                        digits = []
                    if mulStack:
                        for p in mulStack:
                            num *= p
                        mulStack = []
                    addStack.append(num)
            i += 1
        if not digits and not mulStack: return sum(addStack)
        num = 1
        if digits:
            num = self.str2int(digits)
            digits = []
        if mulStack:
            for p in mulStack:
                num *= p
            mulStack = []
        addStack.append(num)
        return sum(addStack)