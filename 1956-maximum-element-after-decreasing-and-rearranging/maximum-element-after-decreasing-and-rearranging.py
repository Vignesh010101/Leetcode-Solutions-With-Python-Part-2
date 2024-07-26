class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maximum=1
        for i in range(1,len(arr)):
            if arr[i]>maximum:
                maximum+=1

        return maximum