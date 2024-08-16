class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        arr=nums.copy()
        for i in range(1,len(nums)):  #Prefix_sum
            nums[i]+=nums[i-1]
        

        def binary_search(nums,x):
            start=0
            end=len(nums)-1 
            while(start<=end):
                mid=(start+end)//2
                if(nums[mid]==x):
                    return(mid)
                elif(nums[mid]>x):
                    end=mid-1
                else:
                    start=mid+1 
            return(start)
        

        ans=[]
        for i in range(0,len(queries)):
            summ=0
            index=binary_search(arr,queries[i])  #to get the index
            if(index==0):
                summ=nums[-1]-(n*queries[i])
            else:
                summ=(index*queries[i])-(nums[index-1])    #for summ of elements before index
                summ+=(nums[-1]-nums[index-1])-((n-index)*queries[i])     #for summ of elements after index
            ans.append(summ)
        return(ans)