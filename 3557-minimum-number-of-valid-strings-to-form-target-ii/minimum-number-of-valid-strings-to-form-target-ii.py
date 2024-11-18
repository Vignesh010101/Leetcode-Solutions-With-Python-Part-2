class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        d, prime = 256,  1000000007
        pow_d = [1] * (len(target) + 1)
        for i in range(1, len(pow_d)):
            pow_d[i] = (pow_d[i - 1] * d) % prime
        h = set()
        for i in words:
            th = 0
            for j in i:
                th = (d * th + ord(j)) % prime
                h.add(th)
        dp = [math.inf] * len(target)
        i = 0
        th = 0
        l = 0
        while i < len(target):
            th = (d * th + ord(target[i])) % prime
            if th in h:
                dp[i] = 1 + (dp[l - 1] if l - 1 >= 0 else 0)
            else:
                while l < i:
                    temp = pow_d[i - l]
                    th = (th - ord(target[l]) * temp) % prime
                    l += 1
                    if th in h:
                        dp[i] = 1 + (dp[l - 1] if l - 1 >= 0 else 0)
                        break
            i += 1
        return (dp[-1] if dp[-1] != math.inf else -1)




            




            