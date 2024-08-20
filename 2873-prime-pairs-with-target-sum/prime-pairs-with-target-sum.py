class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = self.sieveOfEratosthenes(n)  # Generate prime numbers up to n
        res = []

        for p in range(2, n // 2 + 1):
            if is_prime[p] and is_prime[n - p]:
                res.append([p, n - p])

        return res

    def sieveOfEratosthenes(self, n: int) -> List[bool]:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        return is_prime