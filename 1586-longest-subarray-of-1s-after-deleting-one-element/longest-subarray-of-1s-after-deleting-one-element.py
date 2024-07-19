class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        count=0
        max_size=0
        for j in range(len(nums)):
            if nums[j]==0:
                count+=1
            while count>1:
                if nums[i]==0:
                    count-=1
                i+=1
            max_size=max(max_size,j-i)

        return max_size