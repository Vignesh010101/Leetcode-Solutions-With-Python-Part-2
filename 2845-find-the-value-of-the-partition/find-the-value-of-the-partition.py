class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        lst=[]
        for i in range(1,len(nums)):
            c=abs(nums[i]-nums[i-1])
            lst.append(c)
     
        return min(lst)
        