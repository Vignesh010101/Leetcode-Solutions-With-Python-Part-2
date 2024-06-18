class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(num):
            # Key step 2:
            # Only need to check the first sqrt(num) number of divisors
            for i in range(2, int(num ** 0.5) + 1):
                if not num % i: return False
            return True

        if n < 3: return 2
        if 7 < n <= 11: return 11
        i = 2
        while True:
            # Key step 1:
            # Only need to check the number with the odd length of digits
            # Because the only palindrome with the even length of digits is 11
            num = int(str(i) + str(i)[::-1][1:])
            if num >= n and isPrime(num): return num
            i += 1
        