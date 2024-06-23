class Solution:
    N = int(1e9) + 7

    # Function to perform binary exponentiation
    def binary(self, a, b):
        res = 1
        a = a
        while b > 0:
            if b & 1 == 1:
                res = ((res % self.N) * (a % self.N)) % self.N
            a = ((a % self.N) * (a % self.N)) % self.N
            res = res % self.N
            b >>= 1
        return res

    # Function to calculate the number of good partitions
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        s = set()  # Set to store frequency and element
        m = {}  # Dictionary to store frequency of elements

        # Count frequency of each element in the nums array
        for x in nums:
            m[x] = m.get(x, 0) + 1

        count = 0
        i = 0
        n = len(nums)

        # Iterate through the array
        while i < n:
            s.discard((-1 * m[nums[i]], nums[i]))  # Remove frequency and element pair from set
            m[nums[i]] -= 1  # Decrease frequency of the current element

            # If the element still has frequency left, insert it back into the set
            if m[nums[i]] > 0:
                s.add((-1 * m[nums[i]], nums[i]))

            i += 1

            # If the set is empty, increment the count
            if len(s) == 0:
                count += 1

        # Calculate the result using binary exponentiation
        return self.binary(2, count - 1)
        # Equivalent way to calculate result using left shift operator
        # return (1 << (count - 1))

