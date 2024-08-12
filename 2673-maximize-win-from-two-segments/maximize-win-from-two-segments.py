class Solution:
    def maximizeWin(self, pos: List[int], k: int) -> int:
        n = len(pos)
        if k*2+1 >= pos[-1] - pos[0]: return n
        pre = [0] * (n + 1)
        ans = left = 0
        for right, p in enumerate(pos):
            while p - pos[left] > k:
                left += 1
            sz = right - left + 1
            res = sz + pre[left]
            if res > ans: ans = res
            if sz >= pre[right]: pre[right+1] = sz
            else: pre[right+1] = pre[right]
        return ans