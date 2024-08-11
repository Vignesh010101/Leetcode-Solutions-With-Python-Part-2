class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
 
        nums = sorted(zip(nums1, nums2), key = lambda x:-x[1])
            
        heap = []

        for n1,n2 in nums[:k]: heappush(heap,n1)

        ans = (sm:= sum(heap))*n2
       
        for n1,n2 in nums[k:]:
            sm+= n1 - heappushpop(heap,n1)
            ans = max(ans,sm * n2)
                
        return ans