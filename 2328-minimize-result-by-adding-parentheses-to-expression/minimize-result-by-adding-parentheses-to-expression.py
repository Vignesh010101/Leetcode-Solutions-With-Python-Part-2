class Solution:
    def minimizeResult(self, expression: str) -> str:
        k = expression.find('+')
        ans = "inf"
        for i in range(k): 
            for j in range(k+1, len(expression)): 
                cand = f'{expression[:i]}({expression[i:k]}+{expression[k+1:j+1]}){expression[j+1:]}'
                ans = min(ans, cand, key=lambda x: eval(x.replace('(', '*(').replace(')', ')*').strip('*')))
        return ans 