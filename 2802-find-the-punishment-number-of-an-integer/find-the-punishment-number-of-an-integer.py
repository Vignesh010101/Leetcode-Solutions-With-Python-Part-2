class Solution:
    def punishmentNumber(self, n: int) -> int:
        def possible(sum_added,cache_sum, n, target):
            
            if not n:
                return target == sum_added+cache_sum
            num = int(n[0])
            cas = cache_sum

            return possible(sum_added,cas*10+num, n[1:], target) or possible(sum_added+cas,num, n[1:], target)

        ans = 0
        for i in range(1, n+1):
           
            if possible(0,0,str(i*i), i):
                ans += i*i
        return ans
            
        