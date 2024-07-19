class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        # Create a frequency dictionary to store remainders
        remainders = {}

        # Count the remainders of each element when divided by k
        for num in arr:
            remainder = num % k
            remainders[remainder] = remainders.get(remainder, 0) + 1

        # Check if the remainders can be paired up to form pairs divisible by k
        if remainders.get(0, 0) % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if remainders.get(i, 0) != remainders.get(k - i, 0):
                return False

        return True
        