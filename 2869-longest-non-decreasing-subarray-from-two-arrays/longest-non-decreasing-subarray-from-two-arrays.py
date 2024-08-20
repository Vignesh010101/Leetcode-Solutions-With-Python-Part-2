class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        curr1 = 1
        curr2 = 1
        ans = 1
        for i in range(1, n):

            prev_curr1 = curr1
            prev_curr2 = curr2

            if nums1[i] >= nums1[i - 1] and nums1[i] >= nums2[i - 1]:
                curr1 = max(prev_curr1 + 1, prev_curr2 + 1)
            elif nums1[i] >= nums1[i - 1]:
                curr1 = prev_curr1 + 1
            elif nums1[i] >= nums2[i - 1]:
                curr1 = prev_curr2 + 1
            else:
                curr1 = 1
            
            if nums2[i] >= nums1[i - 1] and nums2[i] >= nums2[i - 1]:
                curr2 = max(prev_curr1 + 1, prev_curr2 + 1)
            elif nums2[i] >= nums2[i - 1]:
                curr2 = prev_curr2 + 1
            elif nums2[i] >= nums1[i - 1]:
                curr2 = prev_curr1 + 1
            else:
                curr2 = 1
            ans = max(ans, curr1, curr2)

        return ans