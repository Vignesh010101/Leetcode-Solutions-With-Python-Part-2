class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        @cache
        def special(arr):
            for i in range(1, len(arr)):
                if arr[i] % arr[i-1]:
                    return False
            
            return True

        @cache
        def dp(last, free):
            ret = 0
            free, n = sorted(free), len(free)
            temp = free.copy()
            for num in free:
                if not num % last or not last % num:
                    temp.remove(num)
                    if special(tuple(free)): ret += factorial(n-1) % mod
                    else: ret += dp(num, tuple(temp)) % mod
                    temp.append(num)
                    ret %= mod
            
            return ret
        
        return sum(dp(e, tuple(set(nums)-set([e]))) for e in nums) % mod