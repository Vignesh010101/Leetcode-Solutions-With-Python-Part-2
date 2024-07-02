class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=Counter(nums1)
        b=Counter(nums2)
        result=[]
        for i,j in b.items():
            if i in a:
                result.extend([i] * min(j, a[i]))
        return result