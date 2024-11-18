class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        n, dp = len(nums), [nums]

        for i in range(1, n):
                                                        # We compute XOR for the current level
            nums = list(map(xor, nums, nums[1:]))     
            dp.append(nums[:])                          
                                                        # We update the maximum values in dp
            for j in range(len(nums)):                 
                dp[i][j] = max(nums[j], dp[i-1][j], dp[i-1][j+1])
        
        return [dp[r - l][l] for l, r in queries] 