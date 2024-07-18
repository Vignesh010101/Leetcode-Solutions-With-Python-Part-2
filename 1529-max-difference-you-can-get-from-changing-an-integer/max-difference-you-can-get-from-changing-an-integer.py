class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        
        def convert(s, index, target):
            if index >= len(s):
                return s
            if s[index] == target:
                return convert(s, index + 1, '0' if target == '1' else target)
            if index > 0 and s[0] == s[index]:
                return convert(s, index + 1, '0' if target == '1' else target)
            temp = ''.join([x if x != s[index] else target for x in s])
            return temp

        M = int(convert(num, 0, '9'))
        m = int(convert(num, 0, '1'))
        if m == 0:
            m = int(num)
        print(M, m)
        return M - m