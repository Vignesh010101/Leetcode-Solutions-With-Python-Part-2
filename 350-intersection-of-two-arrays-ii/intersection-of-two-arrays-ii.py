class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result=[]
        i=0
        for num in nums1:
            if i>=len(nums2):
                break
            while i<len(nums2)-1 and nums2[i]<num:
                i+=1
            if nums2[i]==num:
                i+=1
                result.append(num)

        return result
