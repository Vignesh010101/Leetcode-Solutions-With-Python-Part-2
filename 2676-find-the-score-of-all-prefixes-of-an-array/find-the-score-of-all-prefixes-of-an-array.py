class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        msf = -1
        for i in range(n):
            if nums[i]>msf:
                msf = nums[i]
            nums[i] = msf + nums[i]
        summ=0
        for i in range (n):
            nums[i] = summ + nums[i]
            summ = nums[i]
        return(nums)


        
        