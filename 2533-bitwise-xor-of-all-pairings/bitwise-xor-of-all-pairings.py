class Solution:        
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        n1 = 0 if not len(nums2)%2 else reduce(xor,nums1)
        n2 = 0 if not len(nums1)%2 else reduce(xor,nums2)
        return n1^n2