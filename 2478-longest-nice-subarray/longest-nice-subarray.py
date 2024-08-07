class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        start=0
        max_nice=0

        for end in range(len(nums)):
            temp=start
            while temp < end :
                if nums[end] & nums[temp] != 0:
                    start=temp+1
                temp+=1
            
            max_nice=max(max_nice,end-start+1)
           
            
        return max_nice
        