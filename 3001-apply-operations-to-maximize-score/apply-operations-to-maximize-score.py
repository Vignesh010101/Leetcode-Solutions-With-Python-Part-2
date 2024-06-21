class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        @lru_cache(None)
        def getPrimeFactors(n):
            res = set()
            
            for i in range(2, isqrt(n) + 1):
                while n % i == 0:
                    res.add(i)
                    n //= i
            
            if n > 1: res.add(n)
            return len(res)
        
        arr = [getPrimeFactors(i) for i in nums]
        
        f = [len(arr) - i - 1 for i in range(len(arr))]
        st = []
        
        for i in range(len(arr)):
            while st and arr[st[-1]] < arr[i]:
                t = st.pop()
                f[t] = i - t - 1
            st.append(i)
        
        b = [len(arr) - i - 1 for i in range(len(arr) - 1, -1, -1)]
        st = []
        
        for i in range(len(arr) - 1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                t = st.pop()
                b[t] = t - i - 1
            st.append(i)
        
        hp = []
        for i in range(len(arr)):
            t1 = f[i] + 1
            t2 = b[i] + 1
            hp.append( (t1 * t2, nums[i]) )
        
        hp.sort(key = lambda x: (-x[1], -x[0]))
        res = 1
        mod = pow(10, 9) + 7
        
        for i, j in hp:
            t = min(i, k)
            k -= t
            
            res = (res * pow(j, t, mod)) % mod
            
            if k == 0:
                break
                
        return res