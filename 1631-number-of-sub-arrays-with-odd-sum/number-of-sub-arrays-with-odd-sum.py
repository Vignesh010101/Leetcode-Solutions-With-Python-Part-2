class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even = 1 #(sum zero before array start)
        odd = 0
        rsum = 0
        for i in range(len(arr)):
            rsum += arr[i]
            if rsum % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % (10**9 + 7)