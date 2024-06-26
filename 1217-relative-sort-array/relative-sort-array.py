class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set=set(arr2)
        nums1=[]
        nums2=[]

        for i in arr1:
            if i in arr2_set:
                nums1.append(i)
            else:
                nums2.append(i)

        count=Counter(nums1)

        result=[]
        for i in arr2:
            result+=[i]*count[i]

        return result+sorted(nums2)
            