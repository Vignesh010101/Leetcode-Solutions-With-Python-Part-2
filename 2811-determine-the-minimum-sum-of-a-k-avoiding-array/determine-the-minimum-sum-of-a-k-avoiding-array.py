class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        minNum = k // 2
        if n < minNum:
            return (n*n + n) // 2
        
        res = ((minNum*minNum) + minNum) // 2
        n -= minNum

        while n > 0:
            res += k
            n -= 1
            k += 1
        
        return res
        