class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_pos = expression.find('+')
        min_val, min_lp, min_rp = None, 0, 0

        for lp in range(0, plus_pos):
            for rp in range(plus_pos+2, len(expression)+1):
                val = int(expression[:lp] or 1) * \
                    (int(expression[lp:plus_pos]) + int(expression[plus_pos+1:rp])) * \
                    int(expression[rp:] or 1)
                if min_val is None or val < min_val:
                    min_val = val
                    min_lp = lp
                    min_rp = rp
        
        return expression[:min_lp] + '(' + expression[min_lp:min_rp] + ')' + expression[min_rp:]