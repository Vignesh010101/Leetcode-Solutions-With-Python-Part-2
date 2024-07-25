class Solution:
    def maxValue(self, n: int, index: int, ms: int) -> int:

        def helper(m):  # return bool, possible to raise nums[index] by m?
            need = m

            # left
            leftb = index - (m - 1)
            need += ((m - 1) * m) // 2
            if leftb < 0:
                tmp = abs(leftb)
                offset = (tmp * (tmp + 1)) // 2
                need -= offset

            # right
            rightb = index + (m - 1)
            need += ((m - 1) * m) // 2
            if rightb >= n:
                tmp = rightb - (n - 1)
                offset = (tmp * (tmp + 1)) // 2
                need -= offset

            return need <= remain

        remain = ms - n
        l, r = 0, remain
        ans = 0

        if helper(r): # can take max value initially
            return r + 1

        while l < r:
            m = (l + r) // 2

            if helper(m):  # possible to take
                ans = max(ans, m)
                l = m + 1
            else:
                r = m
        return ans + 1