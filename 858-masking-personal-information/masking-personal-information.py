class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            ss = s.split('@')
            return ss[0][0] + '*****' + ss[0][-1] + '@' + ss[1]
        
        k = len([int(x) for x in s if x.isdigit()]) - 10
        res, local_num = '+' + '*'*k + '-' if k > 0 else '', '' 
        idx = -1
        while len(local_num) < 4:
            if (ch := s[idx]).isdigit():
                local_num += ch
            idx -= 1
        res += '***-***-' + local_num[::-1]

        return res