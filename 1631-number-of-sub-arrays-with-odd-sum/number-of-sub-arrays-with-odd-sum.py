class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 0
        vk = 0
        ans = 0
        for num in arr:
            vk+=num
            vk%=2
            if vk==1:
                odd += 1
                ans += 1+even
            else:
                even += 1
                ans += odd
            ans%=MOD
        
        return ans