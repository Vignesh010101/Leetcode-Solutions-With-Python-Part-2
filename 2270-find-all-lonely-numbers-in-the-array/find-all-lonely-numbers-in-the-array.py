class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        num_set=set(nums)
        a=[]
        for i in range(len(nums)):
            if nums[i]-1 in num_set or nums[i]+1 in num_set:
                pass
            else:
                a.append(nums[i])
        c=Counter(a)
        d=list(c.items())
        x=[]
        for i in range(len(d)):
            if d[i][1]==1:
                x.append(d[i][0])
        return x