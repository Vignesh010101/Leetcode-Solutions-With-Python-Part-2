class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @cache
        def rec(pos, c):
            if pos==n:
                return 0
            elif c==0:
                m = max(nums[pos:])
                s = sum(nums[pos:])
                return m*(n-pos)-s

            ret = float('inf')
            m = nums[pos]
            s = 0
            for i in range(pos, n):
                m = max(m, nums[i])
                s += nums[i]
                ret = min(ret, m*(i-pos+1)-s + rec(i+1, c-1))
            return ret

        return rec(0, k)



                