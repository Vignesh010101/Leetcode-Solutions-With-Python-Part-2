class Solution(object):
    def minFlips(self, target):
        if '1' not in target:
            return 0
        ok = '0'
        ans, i, n = 0, target.find('1'), len(target)
        while i<n:
            if ok != target[i]:
                ans += 1
                ok = target[i]
            i += 1
        return ans

        